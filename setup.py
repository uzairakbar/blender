#!/usr/bin/env python

from setuptools import setup

setup(name='blender',
      version='0.1',
      description='Pre-built Blender 2.79 as a python3.5 module bpy for linux.',
      author='Uzair Akbar',
      author_email='uzairakbar@outlook.com',
      url='https://github.com/uzairakbar/blender/archive/v0.1.tar.gz',
      packages=['blender'],
      include_package_data=True
      )
