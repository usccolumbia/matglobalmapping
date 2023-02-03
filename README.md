# matglobalmapping
### Global mapping of inorganic materials

By Qinyang Li at Machine Learning and Evolution Laboratory
by <a href="http://mleg.cse.sc.edu" target="_blank">Machine Learning and Evolution Laboratory</a>, University of South Carolina.

Cite our work: <br>


### Introduction

- Usage: There are 2 section of our code. You can create new feature from all the descriptors or reproduce our mapping results shown in paper.
1. generate features
    generate all the descriptors feature vector for given group of materials structure infomation in format of .cif


2. reproduce the mapping graph
Due to the size of the generated feature the dataset avaliable in this respository is the result from T-SNE. It only contains the xy coordniates for each map.

    -2.0 For global density and property analysis, The dataset avaliable in this respository is is enough to reproduce the global distribution map in our paper (figure 2,4,5,6)

For target group analysis WRT. global distribution, there are 2 senerios. 

    -2.1 your target group of materials is from MP dataset with known their MP ids.
The dataset avaliable in this respository is is enough to reproduce the global distribution map in our paper(figure 3)


    -2.2 you have a group of materials not from MP dataset with their structure file as .cif.
This requires you to generate the feature using section 1 of our code.
Then concatenate the generated features with the whole MP feature to run tsne analysis.

For target group analysis WRT. some local distribution:

2.3 make sure your target and backgound materials are feed into the tsne toghether.
make sure the domain of the background materials is larger than the target materials to get a good map.

E.g. {ABC3 materials}<{ternary materials}
    

- Dataset

the whole MP feature of all 7 different descriptors is avaliable at 
https://figshare.com/account/articles/21980081 



- Platform: Python 3.8, For better orginization and customization, the graph generation scripts is in jupyter notebooks
Pytorch is required to be installed before running our code. https://pytorch.org/get-started/locally/
Since we used a pretrained model and only doing evaluation, the CPU version of the Pytorch is enough for the job.



# environment and setup

# dataset 

# reproduce results

