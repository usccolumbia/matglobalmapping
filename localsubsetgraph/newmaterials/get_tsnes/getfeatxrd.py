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


ele3  = pd.read_csv("./3ele_mp_props.csv")

ele3mpid = ele3['mp_id']


xrd_feat_raw    =  pd.read_csv('../../original_features/mp_xrd_features_data_smooth.csv')


xrd_feat_index = xrd_feat_raw['mp_id'].to_frame()
XRD_string = xrd_feat_raw['XRD'].fillna("[0.0 0.0 0.0]")
xrd_feat_list = []
for line in XRD_string:
    line= str(line)[2:-1]
    lis = list(line.split(" "))
    #print(lis)
    lis = [i for i in lis if i]
    floa = [float(x) for x in lis]
    xrd_feat_list.append(floa)

xrd_feat=pd.DataFrame(xrd_feat_list)
xrd_feat.insert(0, 'mp_id', xrd_feat_index['mp_id'])

select_data= pd.merge(right=xrd_feat, 
                    left=ele3mpid, 
                    how='left', 
                    right_on='mp_id', 
                    left_on='mp_id')
pwdm_aline_feat = select_data


target_tsne = np.nan_to_num(pwdm_aline_feat.iloc[:,1:])

print("data processed")
#print(target_tsne)
tsne = visual(target_tsne)
print("tsne done")
np.save("3ele_xrd_tsne.npy", tsne)
print("xrd_tsne.npy saved")