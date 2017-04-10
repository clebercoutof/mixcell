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

DEVICENAME                  = "/dev/ttyUSB0".encode('utf-8')                                    # Check which port is being used on your controller

ADDR_TORQUE_MAX = 14  
ADDR_CW_ANGLE_LIMIT=6                           # Dynamixel moving status threshold
ADDR_CCW_ANGLE_LIMIT=8
ADDR_D_GAIN = 26
ADDR_I_GAIN = 27
ADDR_P_GAIN = 28
ADDR_DRIVE_MODE = 10

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

print("Dynamixel ID[%s] info" % DXL_ID)

D_GAIN = dynamixel.read1ByteTxRx(port_num, PROTOCOL_VERSION, DXL_ID, ADDR_D_GAIN)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
else:
    print ("D GAIN VALUE: %s" % str(D_GAIN))

I_GAIN = dynamixel.read1ByteTxRx(port_num, PROTOCOL_VERSION, DXL_ID, ADDR_I_GAIN)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
else:
    print ("I GAIN VALUE: %s" % str(I_GAIN))

P_GAIN = dynamixel.read1ByteTxRx(port_num, PROTOCOL_VERSION, DXL_ID, ADDR_P_GAIN)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
else:
    print ("P GAIN VALUE: %s" % str(P_GAIN))

cw_angle_limit = dynamixel.read2ByteTxRx(port_num, PROTOCOL_VERSION, DXL_ID, ADDR_CW_ANGLE_LIMIT)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
else:
    print("CW angle limit is: %s " % cw_angle_limit)

ccw_angle_limit = dynamixel.read2ByteTxRx(port_num, PROTOCOL_VERSION, DXL_ID, ADDR_CCW_ANGLE_LIMIT)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
else:
    print("CCW angle limit is: %s " % ccw_angle_limit)

DRIVE_MODE = dynamixel.read1ByteTxRx(port_num, PROTOCOL_VERSION, DXL_ID, ADDR_DRIVE_MODE)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
else:
    print ("DRIVE MODE VALUE: %s" % str(DRIVE_MODE))

MAX_TORQUE = dynamixel.read2ByteTxRx(port_num, PROTOCOL_VERSION, DXL_ID, ADDR_TORQUE_MAX)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
else:
    print("Torque limit is is: %s " % MAX_TORQUE)

# Close port
dynamixel.closePort(port_num)