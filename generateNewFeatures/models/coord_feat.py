from pymatgen.core.structure import Structure
import numpy as np


tmp = 0

def gen_coord_feat(files):
    df_Fcoord = {}
    df_Ccoord ={}
    
    for file in files:
        struct=Structure.from_file(file)
        fcoords = []
        ccoords = []
        mp_id = file.split('.')[0]

        for s in struct.sites:
            cxyz=s.coords
            fxyz=[s.a , s.b, s.c]
            ccoords.append(cxyz)
            fcoords.append(fxyz)
        ccoords = np.asarray(ccoords)
        fcoords = np.asarray(fcoords)


        placehoder = [[0.0, 0.0, 0.0]]
        i = len(ccoords)
        while i < 444:
            #print(i)
            ccoords= np.vstack((ccoords, placehoder))
            i = len(ccoords)
        df_Ccoord[mp_id] = list(ccoords.flatten())
        
        i = len(fcoords)
        while i < 444:
            #print(i)
            fcoords= np.vstack((fcoords, placehoder))
            i = len(fcoords)
        df_Ccoord[mp_id] =  list(fcoords.flatten())

    return df_Fcoord,df_Ccoord


