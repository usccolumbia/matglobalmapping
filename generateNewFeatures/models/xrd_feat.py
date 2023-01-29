
#Programmed by Jianjun Hu, USC
from __future__ import division
from os import listdir
from os.path import isfile, join
import pickle as pickle
import numpy as np
from pymatgen.core.structure import Structure
import pandas as pd
import pymatgen.analysis.diffraction.xrd as xrd
import itertools
from scipy.stats import gaussian_kde
from pymatgen.analysis.diffraction.xrd import XRDCalculator

#input folder
mypath = "../input_data/cif/"
onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]


def smooth(lt):
    X_data = list(itertools.chain.from_iterable([[x[0]] * int(x[1] * 10) for x in lt]))
    X_plot = np.linspace(0, 90, 901)
    kde = gaussian_kde(X_data, bw_method=.01)
    output = kde.evaluate(X_plot)
    #print(len(output))
    return output

def convert_to_powder(file):
    crystal_struct = Structure.from_file(file)
    powd = xrd.XRDCalculator()
    powd_patt = powd.get_pattern(crystal_struct)
    return [[x,y] for x,y in zip(powd_patt.x,powd_patt.intensity)]


def get_xrd_feat(files):
    xrd_feat={}
    for file in files:
        mp_id = file.split("/")[-1].split(".")[0]
        structure = Structure.from_file(file)
        #print(tmp,structure.formula)
        mpid = file.split("/")[-1].split(".")[0]
        formula = structure.formula



        feature = smooth(convert_to_powder(file))
        xrd_feat[mp_id] = feature


    #print(xrd_feat)
    return xrd_feat

#get_xrd_feat(onlyfiles)

