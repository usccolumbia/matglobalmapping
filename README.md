# Matglobalmapping
### Global mapping of inorganic materials

By Qinyang Li at <a href="http://mleg.cse.sc.edu" target="_blank">Machine Learning and Evolution Laboratory</a>, University of South Carolina.

Cite our work: Qinyang Li, Rongzhi Dong, Nihang Fu, Lai Wei, Sadman Sadeed Omee，Jianjun Hu*. Global mapping of structures and properties of crystal materials. 2023 Arxiv.xxx<br>


<!-- ![map](globalmap.png) -->
<img src="globalmap.png" width="60%">


### Installation
- Platform: Python 3.8, For better orginization and customization, the graph generation scripts is in jupyter notebooks
1. Create your own conda or other enviroment.
2. install basic packages
```
conda create --name globalmapping python=3.8 
conda activate globalmapping

pip install -r requirements.txt
```
3. Install `pytorch` from [pytorch website](https://pytorch.org/get-started/previous-versions/) given your python & cuda version
Since we used a pretrained model and only doing evaluation, the CPU version of the Pytorch is enough for the job.

### Datasets

Raw datasets, the whole MP feature datasets of all 7 different descriptors, and global map t-sne processed map datasets are avaliable at [dataset](dataset/) folder. 


### Usage
There are 2 section of our code. You can create new feature from all the descriptors or reproduce our mapping results shown in paper.
1. Generate all the descriptors feature vector for given group of materials structure infomation in format of .cif

    - [generate features](https://github.com/usccolumbia/matglobalmapping/tree/main/generateNewFeatures)

2. Reproduce the mapping graph 
For global density and property analysis, The dataset avaliable in this respository is is enough to reproduce the global distribution map in our paper (figure 2,4,5,6).Due to the size of the generated feature the dataset avaliable in this respository is the result from T-SNE. It only contains the xy coordniates for each map.

    - [global density](https://github.com/usccolumbia/matglobalmapping/blob/main/graphsgenerate/allMP_global_density.ipynb) 
    - [global property](https://github.com/usccolumbia/matglobalmapping/blob/main/graphsgenerate/allMP_global_property.ipynb) 
      

For target group analysis WRT. global distribution, there are 2 senerios. (figure 3)

- your target group of materials is from MP dataset with known their MP ids.The dataset avaliable in this respository is is enough to reproduce the global distribution map in our paper
    - [custom list of mpid](https://github.com/usccolumbia/matglobalmapping/tree/main/globalgraph/mpid_over_global)

- you have a group of materials not from MP dataset with their structure file as .cif. This requires you to generate the feature using section 1 of our code.Then concatenate the generated features with the whole MP feature to run tsne analysis.
        
    - [generate features](https://github.com/usccolumbia/matglobalmapping/tree/main/generateNewFeatures)
    - [custom materials](https://github.com/usccolumbia/matglobalmapping/tree/main/localsubsetgraph/newmaterials)


For target group analysis WRT. some local distribution:

- Make sure your target and backgound materials are feed into the tsne toghether.Make sure the domain of the background materials is larger than the target materials to get a good map.E.g. {ABC3 materials}<{ternary materials}

    - [custom scope](https://github.com/usccolumbia/matglobalmapping/tree/main/generateNewFeatures) 

    
### Sample global maps of inorganic materials








