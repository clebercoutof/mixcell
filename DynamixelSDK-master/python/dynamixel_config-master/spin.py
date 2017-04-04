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

os.sys.path.append('../dynamixel_functions_py')             # Path setting

import dynamixel_functions as dynamixel                     # Uses Dynamixel SDK library

# Protocol version
PROTOCOL_VERSION            = 1                             # See which protocol version is used in the Dynamixel
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

goal_position                    = raw_input("Input the servo's goal position:")                     #Servo actual BAUDRATE
try:
    goal_position = int(goal_position)
except ValueError:
    print("Invalid number")


DEVICENAME                  = "/dev/ttyUSB0".encode('utf-8')                                    # Check which port is being used on your controller

ADDR_MOVING_SPEED          = 32
ADDR_GOAL_POSITION          = 30

COMM_SUCCESS                = 0                             # Communication Success result value
COMM_TX_FAIL                = -1001                         # Communication Tx Failed

# Initialize PortHandler Structs
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
port_num = dynamixel.portHandler(DEVICENAME)

# Initialize PacketHandler Structs
dynamixel.packetHandler()

dxl_comm_result = COMM_TX_FAIL                              # Communication result

# Open port
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


dynamixel.write2ByteTxRx(port_num, PROTOCOL_VERSION, DXL_ID, ADDR_MOVING_SPEED, goal_position)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
else:
    if goal_position >= 1024:
        goal_position = (goal_position - 1023)* 0.11
        print("The motor is moving at the CW direction with %srpm" % goal_position)
    else:
        goal_position = goal_position * 0.11
        print("The motor is moving at the CCW direction with %srpm" % goal_position)


# Close port
dynamixel.closePort(port_num)