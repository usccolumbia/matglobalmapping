import numpy as np
from feature import *
from config import *
from structure import *
import pandas as pd
small = 0.0001
cut = 8.0
rs = 0.25
# change it to your data directory
#data_dir = "../../input_data/poscar/"
dt = np.dtype([('typ', 'S2'), ('pos', float, (3, ))])
lth = int(np.rint(cut/rs))
# feature name
fname = "feature_topo_compo"








def get_id_list(data_dir):
    allmp_id = pd.read_csv(data_dir + 'targets.csv')
    id_list = allmp_id.iloc[:, 0].tolist()

    return id_list