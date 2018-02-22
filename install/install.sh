#!/bin/bash

wget https://github.com/ROBOTIS-GIT/DynamixelSDK/archive/3.4.3.tar.gz
tar xvzf 3.4.3.tar.gz
rm -rf 3.4.3.tar.gz
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
cd install/DynamixelSDK-3.4.3/c/build/linux64/
make
sudo make install
cd -
cd install/
rm -rf DynamixelSDK-3.4.3/


