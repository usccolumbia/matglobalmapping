
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
from math import sin, cos, asin, pi, degrees, radians
import numpy as np
from pymatgen.analysis.diffraction.xrd import XRDCalculator



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



XRD= XRDCalculator(wavelength="CuKa", symprec=0, debye_waller_factors=None)

def get_vae_feat(file):
    feature = smooth(convert_to_powder(open(file, 'rb').read()))
    return feature




    

