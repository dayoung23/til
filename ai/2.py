import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn. init as init
import torch.utils.data as data
import torchvision.datasets as dset
import torchvision. transforms as transforms
from torch. utils. data import DataLoader

batch_size=1
learning_rate = 0.0002
num_epoch = 100