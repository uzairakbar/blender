#!/usr/bin/env python
from setuptools import setup
from io import open

# Get the long description from the README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='blender',
      version='1.4',
      description='Pre-built Blender 2.79 as a python3.5 module bpy for linux.',
      author='Uzair Akbar',
      author_email='uzairakbar@outlook.com',
      url='https://github.com/uzairakbar/blender/archive/v1.4.tar.gz',
      packages=['blender'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      include_package_data=True
      )
