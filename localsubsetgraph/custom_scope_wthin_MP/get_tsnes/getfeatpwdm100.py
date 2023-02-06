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


pwdm_feat_raw    =  pd.read_csv('../../original_features/mp_distmatrix_feature.csv')


pwdm_feat_index = pwdm_feat_raw['mp_id'].to_frame()
pwdm_string = pwdm_feat_raw['feature'].fillna("[0.0 0.0 0.0]")
pwdm_feat_list = []
for line in pwdm_string:
    line= str(line)[2:-1]
    lis = list(line.split(" "))
    #print(lis)
    lis = [i for i in lis if i]
    floa = [float(x) for x in lis]
    pwdm_feat_list.append(floa)

pwdm_feat=pd.DataFrame(pwdm_feat_list)

pwdm_feat.insert(0, 'mp_id', pwdm_feat_index['mp_id'])


select_data= pd.merge(right=pwdm_feat, 
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
np.save("3ele_pwdm_tsne.npy", tsne)
print("pwdm_tsne.npy saved")