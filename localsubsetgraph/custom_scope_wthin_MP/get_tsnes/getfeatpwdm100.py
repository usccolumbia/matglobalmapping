import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import matplotlib as mpl
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

def visual(X):
    
    
    tsne = manifold.TSNE(n_components=2, verbose=1, perplexity=30, n_iter=400,random_state=501)
    X_tsne = tsne.fit_transform(X)

    
    print("Org data dimension is {}. Embedded data dimension is {}".format(X.shape[-1], X_tsne.shape[-1]))

    #'''嵌入空间可视化'''
    x_min, x_max = X_tsne.min(0), X_tsne.max(0)
    X_norm = (X_tsne - x_min) / (x_max - x_min)
    

    return  X_norm


ele3  = pd.read_csv("../background_mp_ids.csv")
ele3mpid = ele3['mp_id']


#pwdm_dir  =  '../../../../motif_analysis/phase5/original_features/pwdm100.npy'
pwdm_dir =  '../../whole_MP_feat/pwdm100.npy'


pwdm100_raw      = np.load(pwdm_dir,allow_pickle=True).item()
pwdm100_feat = pd.DataFrame.from_dict(pwdm100_raw, orient='index')
pwdm100_feat.reset_index(inplace=True)
pwdm100_feat = pwdm100_feat.rename(columns = {'index':'mp_id'})



select_data= pd.merge(right=pwdm100_feat, 
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
np.save("../tsne/custom_pwdm_tsne.npy", tsne)
print("tsne saved")