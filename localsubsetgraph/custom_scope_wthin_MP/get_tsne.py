import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
import os
from os import listdir
from os.path import isfile, join



onlyfiles = [ f for f in listdir("./get_tsnes") if isfile(join("./get_tsnes", f))]
os.chdir("./get_tsnes")
for files in onlyfiles:
    print(files.split(".")[0])
    os.system(f"python "+files)
