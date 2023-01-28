from pymatgen.core.composition import Composition
from pymatgen.core.structure import Structure

from os import listdir
from os.path import isfile, join

import pandas as pd

mypath = './cif/'
materialdf = pd.DataFrame()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
    file = f"{mypath}/{file}"
    mpid = file.split("/")[-1].split(".")[0]
    structure = Structure.from_file(file)
    formu = str(structure).split("\n")[1].split(":")[1]
    
    new_row = {'mp_id':mpid, 'formula':formu}
    materialdf = materialdf.append(new_row, ignore_index=True)
#print(materialdf)
materialdf.to_csv("mp_id.csv",index=False)
