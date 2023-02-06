import sys
import os
#import deeperGATGNN.main as deepgatgnn

from os import listdir
from os.path import isfile, join
import argparse
import runpy

def gen_target(mypath):
    
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    with open(mypath+'/targets.csv', 'w') as f:
        for file in onlyfiles:
            file = f"{mypath}/{file}"
            mpid = file.split("/")[-1].split(".")[0]
            f.write(mpid+','+str(0) + '\n')


gen_target('../../input_data/cif')
os.system(f"python ./main.py --data_path=../../input_data/cif --run_mode=Analysis --model_path=./super_gatgnn_gc20_bulk_model.pth --format=cif")
#gatgnn()







