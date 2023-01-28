
#Programmed by Jianjun Hu, USC
from __future__ import division
from os import listdir
from os.path import isfile, join
import pickle as pickle
import glob,os,sys,csv
import numpy as np
import string
from pymatgen.core import Element
from pymatgen.core import Composition
from pymatgen.core.structure import Structure
from pymatgen.ext.matproj import MPRester
import pandas as pd
import re
import pymatgen.analysis.diffraction.xrd as xrd
import itertools
from scipy.stats import gaussian_kde
from shutil import copyfile,move

#input folder
mypath = "./input_data"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles[0:10])


def smooth(lt):
    X_data = list(itertools.chain.from_iterable([[x[0]] * int(x[1] * 10) for x in lt]))
    X_plot = np.linspace(0, 90, 901)
    kde = gaussian_kde(X_data, bw_method=.01)
    output = kde.evaluate(X_plot)
    return output

def convert_to_powder(cif_str):
    crystal_struct = Structure.from_file(file)
    powd = xrd.XRDCalculator()
    powd_patt = powd.get_pattern(crystal_struct)
    return [[x,y] for x,y in zip(powd_patt.x,powd_patt.intensity)]



import os
import json
from math import sin, cos, asin, pi, degrees, radians
import pymatgen as mg
import numpy as np
import matplotlib.pylab as plt
from pymatgen.analysis.diffraction.xrd import XRDCalculator
XRD= XRDCalculator(wavelength="CuKa", symprec=0, debye_waller_factors=None)
n = len(onlyfiles)
df = pd.DataFrame(index=range(n),columns=range(903))

tmp = 0
for file in onlyfiles:
    file = f"{mypath}/{file}"

    structure = Structure.from_file(file)
    print(tmp,structure.formula)
    mpid = file.split("/")[-1].split(".")[0]
    formula = structure.formula
    feature = smooth(convert_to_powder(open(file, 'rb').read()))


    df.iloc[tmp,0] = mpid 
    df.iloc[tmp,1] = formula
    df.iloc[tmp,2:] = feature   
    tmp += 1

    
df.to_csv('xrd_features_data.csv',index = None)

