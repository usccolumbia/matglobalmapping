from pymatgen.core.structure import Structure
import numpy as np

df_Fcoord = {}
df_Ccoord ={}
tmp = 0

def gen_coord_feat(file):

    struct=Structure.from_file(file)
    fcoords = []
    ccoords = []
    mp_id = file.split('.')[0]
    
    for s in struct.sites:
        cxyz=s.coords
        fxyz=[s.a , s.b, s.c]
        ccoords.append(cxyz)
        fcoords.append(fxyz)
    df_Ccoord = np.asarray(ccoords)
    df_Fcoord = np.asarray(fcoords)

    
    placehoder = [[0.0, 0.0, 0.0]]
    i = len(df_Ccoord)
    while i < 444:
        #print(i)
        df_Ccoord= np.vstack((df_Ccoord, placehoder))
        i = len(df_Ccoord)
    df_Ccoord_0pad =  list(df_Ccoord.flatten())

    i = len(df_Fcoord)
    while i < 444:
        #print(i)
        df_Fcoord= np.vstack((df_Fcoord, placehoder))
        i = len(df_Fcoord)
    df_Fcoord_0pad =  list(df_Fcoord.flatten())

    return df_Ccoord_0pad,df_Fcoord_0pad


