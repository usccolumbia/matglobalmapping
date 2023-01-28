import sys
import os
import deeperGATGNN.main as deepgatgnn

from os import listdir
from os.path import isfile, join
import argparse
import runpy

def gen_target():
    mypath ="./input_data"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    with open(mypath+'/targets.csv', 'w') as f:
        for file in onlyfiles:
            file = f"{mypath}/{file}"
            mpid = file.split("/")[-1].split(".")[0]
            f.write(mpid+','+str(0) + '\n')




def gatgnn():
    inputdir = "../../input_data"
    model_path = "../gatgnn_utils/super_gatgnn_gc20_bulk_model.pth"
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default = inputdir)
    parser.add_argument("--run_mode", default = "Analysis")
    parser.add_argument("--model_path", default = model_path)
    parser.add_argument('--format',  default = "cif")
    args = parser.parse_args()
  
    
    #runpy.run_path(path_name='./models/deeperGATGNN/main.py --data_path='+inputdir+' --model_path='+model_path)

    deepgatgnn.main(inputdir,model_path) 


gatgnn()







