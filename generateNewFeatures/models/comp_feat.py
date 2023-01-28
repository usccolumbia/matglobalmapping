import os
import math
import json
import pickle
import itertools
import numpy as np
# np.random.seed(123)
import pandas as pd
from pymatgen.core.composition import Composition

def build_entry():
    with open('./periodic_table.json') as f:
        d = json.load(f)

    f2no = {}#all elements in periodic table
    for e in d.keys():
        f2no[e] = d[e]["Atomic no"]

    allmp = pd.read_csv('./allmp_formula.csv')
    formulas = allmp.values[:,1]
    #print(df)
    #print(formulas)
    ls = []
    for c in formulas:
        try:
            obj = Composition(c)
            ls += [e.symbol for e in obj.elements]
        except Exception as e:
            pass
       
    elements = list(set(ls)&set(f2no.keys()))


    print(len(elements))
    v2 = {}#all unique elements in some dataset
    for e in elements:
        v2[e] = f2no[e]
    v2 = sorted(v2.items(), key=lambda item: item[1])

    v3 = {}#index re-encoding
    for i, e in enumerate(v2):
        v3[e[0]] = i
    return v3

def get_onehot_matrix(l=32):
    onehot = build_entry()
    df = pd.read_csv('../../input_data/mp_id.csv')
    df = df.fillna("NaN")
    mpids = df.values[:,0]
    formulas = df.values[:,1]
    data = {}
    for i,c in enumerate(formulas):
        #print(c)
        obj = Composition(c)
        d = obj.as_dict()
        print(max(d.values()))
        if max(d.values()) <= l:
            matrix = np.zeros((len(onehot), l))
            for symbol in d.keys():
                matrix[onehot[symbol],int(d[symbol])-1] = 1
            matrix = np.expand_dims(matrix, -1)
            data[mpids[i]] = matrix
    return data


def pickle_dataset_onehot():    
    mpid2embedding = get_onehot_matrix(l=32)

    existed_mpids = list(mpid2embedding.keys())
    d = {}
    for mpid in existed_mpids:
        d[mpid] = [mpid2embedding[mpid]]

    with open('./onehot.pickle', 'wb') as f:
        pickle.dump(d, f)


pickle_dataset_onehot()








