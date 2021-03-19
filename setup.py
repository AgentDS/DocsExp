# -*- coding: utf-8 -*-
# @Time    : 3/13/21 12:42 AM
# @Author  : Siqi Liang
# @Contact : zszxlsq@gmail.com
# @File    : setup.py
# @Software: PyCharm
from setuptools import setup, find_packages
from codecs import open
from os import path


def get_readme():
    here = path.abspath(path.dirname(__file__))

    # Get the long description from the README file
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    name="DocsExp",
    version="0.1",
    author="AgentDS",
    author_email="zszxlsq@gmail.com",
    description="a demo for docs development and package management",
    long_description=get_readme(),
    url="https://github.com/AgentDS/DocsExp",
    packages=find_packages(exclude=['docs']),  # TODO: add things in 'exclude'
    install_requires=['torch',
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
