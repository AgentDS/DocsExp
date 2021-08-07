# -*- coding: utf-8 -*-
# @Time    : 3/13/21 2:22 PM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : resnet.py
# @Software: PyCharm
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms


# 3x3 convolution
# here is example to put type of args in function header
def conv3x3(in_channels: int, out_channels: int, stride: int = 1) -> torch.nn.Module:
    return nn.Conv2d(in_channels, out_channels, kernel_size=3,
                     stride=stride, padding=1, bias=False)

def calculate():
    print('this is empty')
    return 'this is empty'

# Residual block
# class ResidualBlock(nn.Module):
#     """Create a single residual block

#     Initialization for a single residual block.

#     Args:
#         in_channels (int):
#         out_channels (int):
#         stride (int):
#         downsample (optinal): Defaults to None.

#     Returns:

#     Raises:
#         ClickException: The HTTP request failed or the HTTP response contained an invalid body.
#     """

#     def __init__(self, in_channels, out_channels, stride=1, downsample=None):
#         super(ResidualBlock, self).__init__()
#         self.conv1 = conv3x3(in_channels, out_channels, stride)
#         self.bn1 = nn.BatchNorm2d(out_channels)
#         self.relu = nn.ReLU(inplace=True)
#         self.conv2 = conv3x3(out_channels, out_channels)
#         self.bn2 = nn.BatchNorm2d(out_channels)
#         self.downsample = downsample

#     def forward(self, x):
#         residual = x
#         out = self.conv1(x)
#         out = self.bn1(out)
#         out = self.relu(out)
#         out = self.conv2(out)
#         out = self.bn2(out)
#         if self.downsample:
#             residual = self.downsample(x)
#         out += residual
#         out = self.relu(out)
#         return out


class MyClass(object):
    """Test for MyClass

    Args:
        num (int): number
        age (int): age of class
        time (int): time of class
    """
    def __init__(self, num, time, age):
        self.num = num
        self.age = age
        self.time = time

