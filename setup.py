# -*- coding: utf-8 -*-
# @Time    : 3/13/21 12:42 AM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : setup.py
# @Software: PyCharm
from setuptools import setup, find_packages

setup(
    name="DocsExp",
    version="0.1",
    author="AgentDS",
    author_email="zszxlsq@gmail.com",
    description="a demo for docs development and package management",
    url="https://github.com/AgentDS/DocsExp",
    packages=find_packages(exclude=()),  # TODO: add things in 'exclude'
    install_requires=['pytorch',
                      'torchvision',
                      'numpy'],
    python_requires='>=3.6',
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
