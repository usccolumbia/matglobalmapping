import shutil, os

new_feat_dir = "../../generateNewFeatures/output/"
dest =  './output'
shutil.copytree(new_feat_dir, dest)


