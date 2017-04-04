#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

os.sys.path.append('../dynamixel_functions_py')                                                 # Path setting

import dynamixel_functions as dynamixel

# Protocol version
PROTOCOL_VERSION            = 1                                                                 # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID                      = raw_input("Input the servo's ID:")                                #Servo ID
try:
    DXL_ID = int(DXL_ID)
except ValueError:
    print("Invalid number")

BAUDRATE                    = raw_input("Input the servo's BAUDRATE:")                     #Servo actual BAUDRATE
try:
    BAUDRATE = int(BAUDRATE)
except ValueError:
    print("Invalid number")

NEW_DXL_ID                  = raw_input("Input the DESIRED ID:")                                #Servo desired ID
try:
    NEW_DXL_ID = int(NEW_DXL_ID)
except ValueError:
    print("Invalid number")

DEVICENAME                  = "/dev/ttyUSB0".encode('utf-8')                                    # Check which port is being used on your controller
                                                                                                 # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0"
ADDR_ID=3                                                                           # Dynamixel moving status threshold
ESC_ASCII_VALUE             = 0x1b

COMM_SUCCESS                = 0                             # Communication Success result value
COMM_TX_FAIL                = -1001                         # Communication Tx Failed

# Get methods and members of PortHandlerLinux or PortHandlerWindows
port_num = dynamixel.portHandler(DEVICENAME)

# Initialize PacketHandler Structs
dynamixel.packetHandler()

if dynamixel.openPort(port_num):
    print("Succeeded to open the port!")
else:
    print("Failed to open the port!")
    print("Press any key to terminate...")
    getch()
    quit()

# Seta a baud rate da porta
if dynamixel.setBaudRate(port_num, BAUDRATE):
    print("Succeeded to change the baudrate!")
else:
    print("Failed to change the baudrate!")
    print("Press any key to terminate...")
    getch()
    quit()

# Set baudrate
dynamixel.write1ByteTxRx(port_num, PROTOCOL_VERSION, DXL_ID, ADDR_ID, NEW_DXL_ID)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
else:
    print("ID CHANGED FROM %s  TO : %s" % (DXL_ID,NEW_DXL_ID))

dynamixel.closePort(port_num)
