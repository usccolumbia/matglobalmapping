##General imports
import csv
import os
print(os.getcwd())
import time
from datetime import datetime
import shutil
import copy
import numpy as np
from functools import partial
import platform

##Torch imports
import torch.nn.functional as F
import torch
from torch_geometric.data import DataLoader, Dataset
from torch_geometric.nn import DataParallel
import torch_geometric.transforms as T
from torch.utils.data.distributed import DistributedSampler
from torch.nn.parallel import DistributedDataParallel
import torch.distributed as dist
import torch.multiprocessing as mp

##Matdeeplearn imports

from matdeeplearn import models
from matdeeplearn import process
from matdeeplearn import training
from matdeeplearn.models.utils import model_summary


##Obtains features from graph in a trained model and analysis with tsne
def analysis(
    dataset,
    model_path,
):

    rank = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    inputs = []

    def hook(module, input, output):
        inputs.append(input)

    #os.chdir('../')
    print(os.getcwd())
    assert os.path.exists(model_path), "saved model not found"
    if str(rank) == "cpu":
        saved = torch.load(model_path, map_location=torch.device("cpu"))
    else:
        saved = torch.load(model_path, map_location=torch.device("cuda"))
    model = saved["full_model"]
    model_summary(model)

    print(dataset)

    loader = DataLoader(
        dataset,
        batch_size=512,
        shuffle=False,
        num_workers=0,
        pin_memory=True,
    )

    model.eval()
    ##Grabs the input of the first linear layer after the GNN
    model.lin_out.register_forward_hook(hook)
    for data in loader:
        with torch.no_grad():
            data = data.to(rank)
            output = model(data)

    inputs = [i for sub in inputs for i in sub]
    inputs = torch.cat(inputs)
    inputs = inputs.cpu().numpy()
    print("Number of samples: ", inputs.shape[0])
    print("Number of features: ", inputs.shape[1])
    print(inputs.shape)
    print(inputs[0])
    print(inputs[0][0])
    print(inputs[0][1])
    print(len(dataset.data.structure_id))
    print(dataset.data.structure_id[2])
    
   # fileName = f'data/last_output/{dataset.data.structure_id[i][0][0]}.csv'
    
    with open('latent_features.csv', 'w') as f:
        writer = csv.writer(f)
        
        for i in range(len(dataset.data.structure_id)):
            vals = list(inputs[i])
            #row = vals.insert(0, dataset.data.structure_id[i][0][0])
            row = dataset.data.structure_id[i][0] + vals
            writer.writerow(row)


    # only works for when targets has one index
    targets = dataset.data.y.numpy()


