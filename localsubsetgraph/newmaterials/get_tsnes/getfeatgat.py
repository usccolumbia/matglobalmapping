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


#gatgnn_feat    =  pd.read_csv('../../original_features/mp_GATGNN_feature_output.csv')




lst = list(range(0,64))
col = ['mp_id']
col = col+lst
gatgnn_feat.columns =col

select_data= pd.merge(right=gatgnn_feat, 
                    left=ele3mpid, 
                    how='left', 
                    right_on='mp_id', 
                    left_on='mp_id')
gatgnn_aline_feat = select_data


target_tsne = np.nan_to_num(gatgnn_aline_feat.iloc[:,1:])

print("data processed")
#print(target_tsne)
tsne = visual(target_tsne)
print("tsne done")
np.save("3ele_gatgnn_tsne.npy", tsne)
print("cod0_tsne.npy saved")