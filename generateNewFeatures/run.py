import warnings
warnings.filterwarnings("ignore")
import os
from os import listdir
from os.path import isfile, join
import numpy as np

from models.comp_feat import get_comp_onehot
from models.coord_feat import gen_coord_feat
from models.pwdm_feat import gen_pwdm_feat
from models.topo_feat import get_topo_feat
from models.xrd_feat import get_xrd_feat

inputdir = "./input_data/cif"
onlyfiles = [join(inputdir, f) for f in listdir(inputdir) if isfile(join(inputdir, f))]

cartcord,factcord = gen_coord_feat(onlyfiles)


if not os.path.exists("./output"):
        os.makedirs("./output")
np.save('./output/input_Ccod_feat.npy', cartcord)

np.save('./output/input_Fcod_feat.npy', factcord)

np.save('./output/input_comp_feat.npy', get_comp_onehot(onlyfiles))

np.save('./output/input_pwdm_feat.npy',gen_pwdm_feat(onlyfiles))
np.save('./output/input_xrd_feat.npy',get_xrd_feat(onlyfiles))
np.save('./output/input_topo_feat.npy',get_topo_feat(inputdir))


