#!/bin/bash

echo "This script will set up your virtual environment for use in cs498ir"


#setting up the PATH bits for use in the script export
export PATH=/software/Jupyterhub/jupyterhub-base-kernel/bin:$PATH
export LD_LIBRARY_PATH=/software/Jupyterhub/jupyterhub-base-kernel/lib

# create virtual environment with the user's username as part

virtualenv cs498ir-virtualenv
source cs498ir-virtualenv/bin/activate

# Install the minimal required packages for jupyter to function into the virtual environment
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools

################################################################
#
# Add any additional dependencies here
#
################################################################
python3 -m pip install jupyter ipykernel ipython numpy scipy sklearn klampt PyOpenGL

git clone https://github.com/krishauser/Klampt-jupyter-extension
cd Klampt-jupyter-extension; make install-user; cd ..
git clone https://github.com/krishauser/Klampt-examples

ipython3 kernel install --user --name cs498ir-virtualenv

