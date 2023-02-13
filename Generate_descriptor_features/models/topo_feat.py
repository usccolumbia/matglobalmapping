#from topo_feat_net.topo_feat_gen import get_topo_feat
from ase import io
from os import listdir
from os.path import isfile, join,pardir
import os
import numpy as np
import pandas as pd
import shutil
# gen poscar

def cif2vaspUsingASE(input_dir):
    """
    ASE seems to do an excellent job with reading cif's.
    It will write out the coordinates in cartesian coordinates.
    """
    onlyfiles = [join(input_dir, f) for f in listdir(input_dir) if isfile(join(input_dir, f))&f.endswith(".cif")]
    outpath = '/'.join(input_dir.split('/')[:-1])+'/poscar/'
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    materialdf = pd.DataFrame()
    for file in onlyfiles:  
    
        atoms = io.read(file)
        filename =file.split('/')[-1].split('.')[0]
        #print(filename)
        new_row = {'mp_id':filename, 'traget':0}
        materialdf = materialdf.append(new_row, ignore_index=True)

        
        atoms.write(outpath+f'{filename}', format = 'vasp')
    materialdf.to_csv(outpath+"targets.csv",index=False)
    shutil.copy('./models/utils/element_properties.csv', outpath)   

    
    return outpath


def get_topo_feat(inputdir):
    poscardir = cif2vaspUsingASE(inputdir)
    print("calcuate topo eature")
    os.system(f"python ./models/topo/topo_feat_gen.py --inputdir {poscardir}")
    print("done")
    #read feat
    featuredir = poscardir +'feature_topo_compo/'
    outputfiles = [join(featuredir, f) for f in listdir(featuredir) if isfile(join(featuredir, f))]
    topo_feat={}
    for file in outputfiles:  
        mp_id = file.split('/')[-1].split('_')[0]
        read =np.load(file)
        topo_feat[mp_id]=read
    
    return topo_feat



#get_topo_feat('../input_data/cif/')