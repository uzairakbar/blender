#!/usr/bin/env python
from setuptools import setup
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='blender',
      version='1.3',
      description='Pre-built Blender 2.79 as a python3.5 module bpy for linux.',
      author='Uzair Akbar',
      author_email='uzairakbar@outlook.com',
      url='https://github.com/uzairakbar/blender/archive/v1.3.tar.gz',
      packages=['blender'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      include_package_data=True
      )
