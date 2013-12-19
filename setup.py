#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

required = ['pycli', 'pyyaml']

setup(
    name='yaml2timeline',
    version=0.1,
    description='Simply converts a YAML document into HTML timeline table.',
    author='Weichong Yang',
    author_email='zonble@gmail.com',
    url='https://github.com/zonble/yaml2timeline',
    packages= ['yaml2timeline'],
    package_dir={'yaml2timeline': 'yaml2timeline'},
    install_requires=required,
    entry_points = {
        'console_scripts': [
            'yaml2timeline=yaml2timeline.yaml2timeline:main'
        ],
    },
    license='MIT'
)
