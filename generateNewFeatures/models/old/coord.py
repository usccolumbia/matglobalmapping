from gemmi import cif 
import numpy as np

def get_coords(file):
    doc = cif.read_file(file)
    block = doc.sole_block()
    coords = []
    loop = block.find(["_atom_site_fract_x","_atom_site_fract_y","_atom_site_fract_z"])
    for site in loop:
        atom  = list(map(float, site))
        coords.append(atom)
    return coords
def get_coord_zero(coord):
    placehoder = [[0.0, 0.0, 0.0]]
    i = len(coord)
    while i < 444:
        #print(i)
        coord= np.vstack((coord, placehoder))
        i = len(coord)
    flatten_list =  list(coord.flatten())
    return flatten_list