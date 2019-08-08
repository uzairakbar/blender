#!/usr/bin/env python
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE/"README.md").read_text()

setup(name='blender',
      version='1.0',
      description='Pre-built Blender 2.79 as a python3.5 module bpy for linux.',
      author='Uzair Akbar',
      author_email='uzairakbar@outlook.com',
      url='https://github.com/uzairakbar/blender/archive/v1.0.tar.gz',
      packages=['blender'],
      long_description=README,
      long_description_content_type="text/markdown",
      include_package_data=True
      )
