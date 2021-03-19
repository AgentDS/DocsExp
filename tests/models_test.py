# -*- coding: utf-8 -*-
# @Time    : 3/19/21 1:49 PM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : models_test.py
# @Software: PyCharm
import unittest
import docsexp.models as models
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms


class torchCNN(nn.Module):
    def __init__(self, num_classes: int = 10):
        super(torchCNN, self).__init__()
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
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out


class ModelsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.in_channels = 16
        cls.out_channels = 32
        cls.stride = 1
        cls.num_classes = 10
        cls.cnn_inputs = torch.zeros(20, 1, 28, 28)  # N,C_in, H_in, W_in
        cls.conv_inputs = torch.zeros(20, cls.in_channels, 28, 28)  # N,C_in, H_in, W_in
        cls.num = 10
        cls.time = 20000
        cls.age = 24

    def test_conv3x3(self):
        conv = models.conv3x3(self.in_channels, self.out_channels, self.stride)
        torch_conv = nn.Conv2d(self.in_channels, self.out_channels, kernel_size=3,
                               stride=self.stride, padding=1, bias=False)
        res = conv(self.conv_inputs)
        torch_res = torch_conv(self.conv_inputs)
        self.assertTrue(torch.equal(torch.tensor(res.shape), torch.tensor(torch_res.shape)))

    def test_ConvNet(self):
        cnn = models.ConvNet(self.num_classes)
        torch_cnn = torchCNN(self.num_classes)
        res = cnn(self.cnn_inputs)
        torch_res = torch_cnn(self.cnn_inputs)
        self.assertTrue(torch.equal(torch.tensor(res.shape), torch.tensor(torch_res.shape)))

    def test_MyClass(self):
        obj = models.MyClass(self.num, self.time, self.age)
        self.assertEqual(obj.num, self.num, msg="MyClass num check")
        self.assertEqual(obj.time, self.time, msg="MyClass time check")
        self.assertEqual(obj.age, self.age, msg="MyClass age check")

