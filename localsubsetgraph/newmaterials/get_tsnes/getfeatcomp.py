import numpy as np
import csv
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import matplotlib as mpl

import pickle

def visual(X):
    
    
    tsne = manifold.TSNE(n_components=2, verbose=1, perplexity=30, n_iter=400,random_state=501)
    X_tsne = tsne.fit_transform(X)

    
    print("Org data dimension is {}. Embedded data dimension is {}".format(X.shape[-1], X_tsne.shape[-1]))

    #'''嵌入空间可视化'''
    x_min, x_max = X_tsne.min(0), X_tsne.max(0)
    X_norm = (X_tsne - x_min) / (x_max - x_min)
    

    return  X_norm





ele3  = pd.read_csv("./3ele_mp_props.csv")
ele3mpid = ele3['mp_id']

ids =  ele3mpid.values.tolist()
print(len(ids))
objects = []
with (open("../../original_features/mp_comp_onehot.pickle", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break
newD = dict(zip(objects[0].keys(), [v[0].flatten() for v in objects[0].values()]))
res = {key: newD[key] for key in newD.keys()
       & ids}

print(len(res))

df = pd.DataFrame.from_dict(res, orient='index')
df['mp_id'] = df.index




select_data= pd.merge(right=df, 
                    left=ele3mpid, 
                    how='left', 
                    right_on='mp_id', 
                    left_on='mp_id')
comp_feat = select_data


target_tsne = np.nan_to_num(comp_feat.iloc[:,1:])

print("data processed")
#print(target_tsne)
tsne = visual(target_tsne)
print("tsne done")
np.save("3ele_comp_tsne.npy", tsne)
print("xrd_tsne.npy saved")