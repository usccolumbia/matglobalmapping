This directory only contains the raw cif datasets and the t-sne processed xy coordniates for each map.

## Raw datasets

all_mp_ids.csv contains all the mp_ids of materials downloaded from the Materials Project database (http://www.materialsproject.org)

ABC3_mp_ids.csv contains the mp_ids of prototype ABC3 materials selected from Materials Project database

ABO3_mp_ids.csv contains the mp_ids of prototype ABO3 materials selected from Materials Project database

Piezoelectric_mp_ids.csv contains the mp_ids of materials with annotated piezoelectric properties from Materials Project database

Users can use these ids to download the cifs from Materials Project database using the Pymatgen API.

## Processed datasets

With the given cifs, we calculate the structural and composition features with 7 different descriptors. 

Due to the size of the dataset, the whole MP feature of all 7 different descriptors is avaliable at 
https://figshare.com/account/articles/21980081

## T-sne map datasets

We applied the t-sne dimension reduction to the feature datasets and obtained the 2D coordinates for all materials in different maps.
