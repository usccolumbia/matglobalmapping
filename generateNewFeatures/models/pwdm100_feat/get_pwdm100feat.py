from os import listdir
from pymatgen.core.structure import Structure
from pymatgen.core.periodic_table import ElementBase, Element
import pymatgen.core as core
from os.path import isfile, join
import pandas as pd
from gemmi import cif
import numpy as np
from scipy.spatial.distance import squareform,pdist
from csv import writer
import math
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

mypath = "./all_mp_id/all_mp_data"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(len(onlyfiles))
tmp = 0
ruler = np.load('pwdm100ruler.npy',allow_pickle=True)

dictmatrix ={}

def upper_tri_indexing(A):
    m = A.shape[0]
    r,c = np.triu_indices(m,1)
    return A[r,c]

for file in onlyfiles:
    tmp += 1
    file = f"{mypath}/{file}"
    mpid = file.split("/")[-1].split(".")[0]


    structure = Structure.from_file(file)
    pairmatrix = structure.distance_matrix


    feat = np.zeros((101,), dtype=int)
    pwdm = upper_tri_indexing(pairmatrix).tolist()
    #print(len(pwdm))
    for site in pwdm:
        index = math.floor(stats.percentileofscore(ruler, site))
        #print(index)
        feat[index] = feat[index] +1
    dictmatrix[mpid] = feat
    if tmp %100==0:
        print(tmp)
        
    if tmp %10000==0:
        #print("save_temp")
        
        np.save('pwdm100_temp.npy', dictmatrix)
 
  
np.save('pwdm100.npy', dictmatrix)
print( "done" )