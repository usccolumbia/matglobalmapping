Under this directory, the Figure 7 in our paper can be reproduced.
Here we shown the example of a local 805 that we mentioned in our paper distributing over the backgound of ABC3 prototypes. 

For t-SNE generation, make sure the raw datasets is downloaded and stored in ../whole_MP_feat. Then run the following command with your conda environment active.


```
python get_tsne.py
```

Visualizing graph

- [graph](https://github.com/usccolumbia/matglobalmapping/blob/main/localsubsetgraph/custom_scope_wthin_MP/listofmpid_over_custom_scope.ipynb)


- if you have a group of materials not from MP dataset with their structure file as `.cif`. This requires you to generate the feature using part 1 of our code, then you can modify the get_tsne scripts to generate map for your group
        
    - [generate features](generateNewFeatures/)
    - [custom scope](custom_scope_wthin_MP/)
