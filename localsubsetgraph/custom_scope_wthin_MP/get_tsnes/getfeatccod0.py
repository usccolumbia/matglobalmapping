import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import matplotlib as mpl


def visual(X):
    
    
    tsne = manifold.TSNE(n_components=2, verbose=1, perplexity=30, n_iter=400,random_state=501)
    X_tsne = tsne.fit_transform(X)

    
    print("Org data dimension is {}. Embedded data dimension is {}".format(X.shape[-1], X_tsne.shape[-1]))

    #'''嵌入空间可视化'''
    x_min, x_max = X_tsne.min(0), X_tsne.max(0)
    X_norm = (X_tsne - x_min) / (x_max - x_min)
    

    return  X_norm


ele3  = pd.read_csv("../3ele_mp_props.csv")

ele3mpid = ele3['mp_id']

coord_0_feat    =  pd.read_csv('../../../aline_feat/Ccod0_aline_feat.csv')




select_data= pd.merge(right=coord_0_feat, 
                    left=ele3mpid, 
                    how='left', 
                    right_on='mp_id', 
                    left_on='mp_id')
cod0_raw_feat = select_data
cod0_feat_index = cod0_raw_feat['mp_id'].to_frame()
cod0_string = cod0_raw_feat['feature']
cod0_feat_list = []
for line in cod0_string:
    line= str(line)[1:-1]
    lis = list(line.split(", "))
    #print(lis)
    lis = [i for i in lis if i]
    #floa = [float(x) for x in lis]
    try:
        floa = [float(x) for x in lis]

    except ValueError as ve:
        print(line)

    cod0_feat_list.append(floa)

cod0_feat=pd.DataFrame(cod0_feat_list)

cod0_feat.insert(0, 'mp_id', cod0_feat_index['mp_id'])

target_tsne = np.nan_to_num(cod0_feat.iloc[:,1:])

print("data processed")
#print(target_tsne)
tsne = visual(target_tsne)
print("tsne done")
np.save("3ele_ccod0_tsne.npy", tsne)
print("codv_tsne.npy saved")