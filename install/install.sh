#!/bin/bash

git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
cd ..
cd QTCode/
cwd=$(pwd)
echo export PATH=\$PATH:$(pwd) >>~/.bashrc
chmod +x mixcell_qt.py 
ln -s mixcell_qt.py mixcell
chmod +x mixcell
source ~/.bashrc
cd ..
cd source_code/
cwd=$(pwd)
echo export PYTHONPATH=\$PYTHONPATH:$(pwd) >>~/.bashrc
source ~/.bashrc
apt-cache search pyqt
sudo apt-get install python-qt4
cd .. 
cd install/DynamixelSDK/c/build/linux64/
make
sudo make install
cd -
cd install/
rm -rf DynamixelSDK/


