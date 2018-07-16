#!/bin/bash

wget https://github.com/ROBOTIS-GIT/DynamixelSDK/archive/3.5.4.tar.gz
tar -xvf 3.5.4.tar.gz
cd DynamixelSDK-3.5.4/c/build/linux64/
sudo make install
cd -
sudo rm -rf DynamixelSDK-3.5.4/
rm -rf 3.5.4.tar.gz
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


