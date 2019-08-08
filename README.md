# bpy
Pre-built Blender 2.79 as a python 3.5 module bpy for linux.

## Dependencies
Note that this repository requires **Python 3.5**. Run [THIS](https://github.com/sobotka/blender/blob/v2.79/build_files/build_environment/install_deps.sh) script to install all Blender dependencies before installing this module.
```bash
wget "https://raw.githubusercontent.com/sobotka/blender/v2.79/build_files/build_environment/install_deps.sh"
chmod +x install_deps.sh
./install_deps.sh
```

## Installation
To install via [pypi](https://pypi.org/project/blender/#description):
```bash
python3 -m pip install blender
```
Alternatively:
```bash
git clone https://github.com/uzairakbar/blender.git
python3 -m pip install path/to/blender
```
