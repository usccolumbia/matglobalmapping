from feature import *
from config import *
from structure import *
from multiprocessing import Pool

import numpy as np
import os

# map feature to get feature function
func_map = {
    "feature_topo_compo": get_feature_topo_compo, 
    "feature_add_s_nobin": get_feature_with_s_nobin, 
    "feature_add_s_nobin_Bar0": get_feature_with_s_nobin_Bar0, 
    "feature_composition": get_feature_composition
}
def batch_handle(id_list):
    for id in id_list:
        get_prim_structure_info(data_dir, id)
        enlarge_cell(data_dir, id)
        get_betti_num(data_dir, id)
        func_map[fname](data_dir, id)



def main():
    id_list = get_id_list(data_dir)

    # get feature


    batch_handle(id_list)
    


if __name__ == '__main__':
    main()



    




