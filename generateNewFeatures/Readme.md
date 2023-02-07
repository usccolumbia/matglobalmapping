the input materials should be in the formate of .cif with the name for its mp id (Material projects)
for generated new materials, them need individual unique names.
they need to be put under the directory ./input_data/cif/ 

In this directory, there is some example input file including the materials with mp id from 170 to 201

with the environment properly installed and input data inplace,
the script can be executed by 

```
python run.py
```

The output of each feature generating function is a dictionary. The keys are filenames or mpids (depend on your input), the values are generated feature vectors.
All generated feature is stored in the output folder in the format of .npy



