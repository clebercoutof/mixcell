# Mixcell - The Dynamixel Configuration Tool for linux!

This program is used to identify dynamixels on your network and configure dynamixel parameters

![mixcell](https://cloud.githubusercontent.com/assets/21127944/26158221/8c964ac8-3af1-11e7-8d05-dc0d2a411292.png)

## Features
* NETWORK SEARCH - Search through the selected baudrates and IDs, identifying the connected servos parameters and models.
* FACTORY RESET -Resets an specified servo to the factory config
* PARAMETERS CONFIG -Configures the following parameters:
```
- ID
- Baudrate
- Torque Max
- Mode 	(Wheel/Joint/Multi Turn)
- CW angle limit / CCW angle limit
- P/I/D Gains
- Drive mode (Reverse/Slave)
```
## Getting Started

Clone the repository

```
$ git clone https://github.com/clebercoutof/mixcell
```

Run the shell script to install the Dynamixel SDK, case there is an error follow the instructions 
in the prerequisites.

Go to the installation folder and run install.sh

```
$ cd mixcell/install/
```

```
$ ./install.sh
```
It's necessary to give your user permanent permissions do access the usb port, so
```
sudo usermod -a -G dialout $USER 
```
And restart your computer

To run mixcell, just open the terminal and type:
```
$ mixcell
```
### Prerequisites
It's necessary to install the linux64 C library of [Dynamixel SDK Version 3.4.3](https://github.com/ROBOTIS-GIT/DynamixelSDK/releases/tag/3.4.3) and the PyQT4. 

You can find the complete installation guide for the SDK [here](http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/)

Download the file and extract in the desired folder

```
$ cd ~/foo/DynamixelSDK-3.4.3/c/build/linux64
```

* Build the library

```
$ make
```

* Case there is an error

```
$ make clean
```

* And

```
$ make
```
* Install the library

```
$ sudo make install
```

* Case there is an error

```
$ sudo make reinstall
```

In order to install PyQT4
```
$ apt-cache search pyqt
```

```
$ sudo apt-get install python-qt4
```

## Code documentation
You can find the complete code documentation at http://mixcell.bitballoon.com

## Built With

* [Wing](https://wingware.com/) - The python IDE
* [QT Designer](https://www.qt.io/ide/) - QT IDE
* [Sphinx](http://www.sphinx-doc.org/en/stable/) - Used to generate the documentation

## Authors

* **Cleber Couto Filho** - *Initial work* - [clebercoutof](https://github.com/clebercoutof)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## References

* Dynamixel SDK Code examples
* [Python Programming](https://pythonprogramming.net/) QT tutorials.

## Acknowledgments
Thanks to [Pedro Xavier](https://github.com/pxalcantara) for full time support and [Henrique Poleselo](https://github.com/hpoleselo) for the documentation support.


