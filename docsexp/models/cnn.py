# -*- coding: utf-8 -*-
# @Time    : 3/13/21 3:05 PM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : cnn.py
# @Software: PyCharm
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

class ConvNet(nn.Module):
    """Convolutional network

    Args:
        num_classes (int): number of output classes

    Example:
        >>> from docsexp.models import ConvNet
        >>> num_classes = 10
        >>> model = ConvNet(num_classes)
    """
    def __init__(self, num_classes=10):
        super(ConvNet, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.fc = nn.Linear(7 * 7 * 32, num_classes)

    def forward(self, x):
        """Forward function for CNN.

        Args:
            x (torch.Tensor): input features
        """
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out
