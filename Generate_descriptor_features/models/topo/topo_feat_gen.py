from feature import *
from config import *
from structure import *
from multiprocessing import Pool
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import os
from optparse import OptionParser
import sys, os, re

#data_dir = "../../input_data/poscar/"
# map feature to get feature function
func_map = {
    "feature_topo_compo": get_feature_topo_compo, 
    "feature_add_s_nobin": get_feature_with_s_nobin, 
    "feature_add_s_nobin_Bar0": get_feature_with_s_nobin_Bar0, 
    "feature_composition": get_feature_composition
}
def batch_handle(data_dir,id_list):
    for id in id_list:
        get_prim_structure_info(data_dir, id)
        enlarge_cell(data_dir, id)
        get_betti_num(data_dir, id)
        func_map[fname](data_dir, id)

def get_topo_feat(data_dir):
    id_list = get_id_list(data_dir)
    batch_handle(data_dir,id_list)
    
'''
def main(data_dir):
    args = sys.argv[1:]
    id_list = get_id_list(data_dir)

    # get feature


    batch_handle(data_dir,id_list)
''' 


if __name__ == '__main__':
    #main("../../input_data/poscar/")
    # Parse cmd line args
    parser = OptionParser( usage = "usage: %prog [options] filename.cif" )
    parser.add_option('-d', '--inputdir', dest = 'inputdir', default = False, help = 'dirtory of the input poscar')
    (options, args) = parser.parse_args()

    data_dir = options.inputdir
    
    id_list = get_id_list(data_dir)
    batch_handle(data_dir,id_list)


    




