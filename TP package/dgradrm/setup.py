#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from setuptools import setup

# load the version from the file
with open("VERSION", 'r') as fic:
    version = fic.read()

# set the parameter of the setup
setup(name='dgradrm', # define the name of the package
version=version,
description='test module dgrad',
author='Rudy Menard',
author_email='rudy.b.menard@gmail.com',
# define some scripts as executable
scripts=['src/TPClasses.py'],
packages=['dgradrm'], # namespace of the package
# define where the package "quantile" is located
package_dir={'dgradrm':'src'},

# some additional data included in the package
data_files = [('.', ['VERSION'])],
# List of dependancies
install_requires= ['numpy',
'matplotlib']
)