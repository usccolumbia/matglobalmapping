from pymatgen.core.structure import Structure
import torch
import torch.nn as nn

cnn1d_1 = nn.Conv1d(in_channels=1, out_channels=1, kernel_size=444, stride=444)


def Get_distmatrix(file):        

    structure = Structure.from_file(file)
    pairmatrix = structure.distance_matrix
    return pairmatrix

def dist_cnn(pairmatrix):
    input_1d = torch.tensor(pairmatrix, dtype = torch.float)
    input_1d = input_1d.unsqueeze(0).unsqueeze(0)
    outcnn=cnn1d_1(input_1d).detach().numpy()[0][0]
    return outcnn