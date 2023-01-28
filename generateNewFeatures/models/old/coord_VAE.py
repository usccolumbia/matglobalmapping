from pyexpat import features
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import ast
import argparse
def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def get_and_init_FC_layer(din, dout):
    li = nn.Linear(din, dout)
    #init weights/bias
    nn.init.xavier_uniform_(li.weight.data, gain=nn.init.calculate_gain('relu'))
    li.bias.data.fill_(0.)
    return li


def get_MLP_layers(dims, doLastRelu):
    layers = []
    for i in range(1, len(dims)):
        layers.append(get_and_init_FC_layer(dims[i-1], dims[i]))
        if i==len(dims)-1 and not doLastRelu:
            continue
        layers.append(nn.ReLU())
    return layers


class PointwiseMLP(nn.Sequential):
    '''Nxdin ->Nxd1->Nxd2->...-> Nxdout'''

    def __init__(self, dims, doLastRelu=False):
        layers = get_MLP_layers(dims, doLastRelu)
        super(PointwiseMLP, self).__init__(*layers)


class GlobalPool(nn.Module):
    '''BxNxK -> BxK'''

    def __init__(self, pool_layer):
        super(GlobalPool, self).__init__()
        self.Pool = pool_layer

    def forward(self, X):
        X = X.unsqueeze(-3)
        X = self.Pool(X)
        X = X.squeeze(-2)
        X = X.squeeze(-2)
        return X

class PointNetGlobalMax(nn.Sequential):
    '''BxNxdims[0] -> Bxdims[-1]'''

    def __init__(self, dims, doLastRelu=False):
        layers = [
            PointwiseMLP(dims, doLastRelu=doLastRelu),
            GlobalPool(nn.AdaptiveMaxPool2d((1, dims[-1]))),
        ]
        super(PointNetGlobalMax, self).__init__(*layers)


class PointNetVanilla(nn.Sequential):

    def __init__(self, MLP_dims, FC_dims, MLP_doLastRelu):
        assert(MLP_dims[-1]==FC_dims[0])
        layers = [
            PointNetGlobalMax(MLP_dims, doLastRelu=MLP_doLastRelu),
        ]
        layers.extend(get_MLP_layers(FC_dims, False))
        super(PointNetVanilla, self).__init__(*layers)


class PointNetVanillaModel(nn.Module):

    def __init__(self, opt):
        super(PointNetVanillaModel, self).__init__()
        self.pointnet = PointNetVanilla(opt.pointnet_mlp_dims, opt.pointnet_fc_dims, opt.pointnet_mlp_dolastrelu)

    def forward(self, data):
        return self.pointnet(data)


def get_vae_feat(coord):

    parser = argparse.ArgumentParser(description="MatDeepLearn inputs")
    parser.add_argument('--pointnet_mlp_dims', type=int, nargs='+', default=[3, 64, 128, 128, 1024], help='Dimensions of the MLP in the PointNet encoder.')
    parser.add_argument('--pointnet_fc_dims', type=int, nargs='+', default=[1024, 512, 512, 512], help='Dimensions of the FC in the PointNet encoder.')
    parser.add_argument("--pointnet_mlp_dolastrelu", type=str2bool, nargs='?', const=True, default=False, help='Apply the last ReLU or not in the PointNet encoder.')
    opt, _ = parser.parse_known_args()


    print(torch.cuda.device_count(), "GPUs will be used for training.")
    device = torch.device("cuda:0")
    ae = PointNetVanillaModel(opt)
    ae = torch.nn.DataParallel(ae)
    ae.to(device)
    input = torch.tensor(coord, dtype = torch.float)
    out = ae(input).detach().cpu().numpy()

    return out
   