import sys
import os
#import deeperGATGNN.main as deepgatgnn

from os import listdir
from os.path import isfile, join
import argparse
import pandas as pd

def gen_target(mypath):
    
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))&f.endswith(".cif")]
    with open(mypath+'/targets.csv', 'w') as f:
        for file in onlyfiles:
            file = f"{mypath}/{file}"
            mpid = file.split("/")[-1].split(".")[0]
            f.write(mpid+','+str(0) + '\n')

def gen_gat_feat(inputdir):
    gen_target(inputdir)
    os.chdir("./models/gatgnn/")
    os.system(f"python ./main.py --data_path=../../{inputdir} --run_mode=Analysis --model_path=./deeper_gatgnn_gc20_connor.pth --format=cif")
    csv = pd.read_csv("./latent_features.csv",index_col= None,header=None)
    csv.columns=["mp_id"]+list(range(64))
    dict = csv.set_index('mp_id').T.to_dict('list')
    os.chdir("../../")
    return dict
