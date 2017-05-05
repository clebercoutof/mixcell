# Mixcell

This program is used to identify dynamixels on your network and configure dynamixel parameters

##Features
* NETWORK SEARCH
Search through the selected baudrates and IDs, identifying the connected servos parameters and models.
* FACTORY RESET
Resets an specified servo to the factory config
* PARAMETERS CONFIG
Configured the following parameters
- ID
- Baudrate
- Torque Max
- Mode 	(Wheel/Joint/Multi Turn)
- CW angle limit / CCW angle limit
- P/I/D Gains
- Drive mode (Reverse/Slave)

## Getting Started

If you have already installed in your system the dynamixel sdk.

Clone the repository

```
$ git clone https://github.com/clebercoutof/mixcell
```
```
$ cd ~/foo/mixcell/QTCode
```
```
$ python mixcell_qt.py
```
### Prerequisites
It's necessary to install the linux64 C library of [Dynamixel SDK](https://github.com/ROBOTIS-GIT/DynamixelSDK).

You can find the complete installation guide [here](https://github.com/ROBOTIS-GIT/DynamixelSDK/wiki/3.2.1.2-C-Linux-(or-Linux-for-SBCs))

Clone the dynamixel sdk 

```
$ git clone https://github.com/ROBOTIS-GIT/DynamixelSDK
```

```
$ cd ~/foo/DynamixelSDK/c/build/linux64
```

* Build the library

```
$ make
```

Case there is an error

```
$ make clean
```

And

```
$ make
```
* Install the library

```
$ sudo make install
```

Case there is an error

```
$ sudo make reinstall
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


