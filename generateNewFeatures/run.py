import warnings
warnings.filterwarnings("ignore")
from os import listdir
from os.path import isfile, join

from models.comp_feat import get_onehot_matrix
from models.coord_feat import gen_coord_feat
from models.pwdm_feat import gen_pwdm_feat
from models.topo_feat import get_topo_feat
from models.xrd_feat import get_xrd_feat

inputdir = "./input_data/cif"
onlyfiles = [join(inputdir, f) for f in listdir(inputdir) if isfile(join(inputdir, f))]

get_onehot_matrix(onlyfiles)
gen_coord_feat(onlyfiles)
gen_pwdm_feat(onlyfiles)
get_xrd_feat(onlyfiles)
get_topo_feat(inputdir)
