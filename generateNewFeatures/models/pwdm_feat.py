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

def upper_tri_indexing(A):
    m = A.shape[0]
    r,c = np.triu_indices(m,1)
    return A[r,c]

ruler = np.load('./models/utils/pwdm100ruler.npy',allow_pickle=True)

def gen_pwdm_feat(files):
    dictmatrix ={}
    for file in files:
        mp_id = file.split('.')[0]
        structure = Structure.from_file(file)
        pairmatrix = structure.distance_matrix

        feat = np.zeros((101,), dtype=int)
        pwdm = upper_tri_indexing(pairmatrix).tolist()

        for site in pwdm:
            index = math.floor(stats.percentileofscore(ruler, site))

            feat[index] = feat[index] +1
        dictmatrix[mp_id] = feat
    return dictmatrix
    dictmatrix[mpid] = feat
