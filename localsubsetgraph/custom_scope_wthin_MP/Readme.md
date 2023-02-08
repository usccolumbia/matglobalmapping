Under this directory, the Figure 7 in our paper can be reproduced.

Here we shown the example of a local 805 that we mentioned in our paper distributing over the backgound of ABC3 prototypes. 

- you have a group of materials not from MP dataset with their structure file as `.cif`. This requires you to generate the feature using part 1 of our code, then you need to concatenate the generated features with the whole MP feature to run tsne analysis.
        
    - [generate features](https://github.com/usccolumbia/matglobalmapping/tree/main/generateNewFeatures)
    - [custom materials](https://github.com/usccolumbia/matglobalmapping/tree/main/localsubsetgraph/newmaterials)
