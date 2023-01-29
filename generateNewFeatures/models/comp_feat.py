import os
import math
import pickle
import numpy as np
import pandas as pd
from pymatgen.core.composition import Composition
from pymatgen.core.structure import Structure


def get_onehot_matrix(onlyfiles):
    l=32
    onehot = np.load('MP_periodic_table.npy', allow_pickle=True).item()
    #print(onehot.item())
    onehot_feat={}
    for file in onlyfiles:
       
        mp_id = file.split("/")[-1].split(".")[0]
        structure = Structure.from_file(file)
        formula = str(structure).split("\n")[1].split(":")[1]
        
        ele_dict = Composition(formula).as_dict()
        if max(ele_dict.values()) <= l:
            matrix = np.zeros((len(onehot), l))
            for symbol in ele_dict.keys():
                matrix[onehot[symbol],int(ele_dict[symbol])-1] = 1
            matrix = np.expand_dims(matrix, -1)
            onehot_feat[mp_id] = matrix
    return onehot_feat





















