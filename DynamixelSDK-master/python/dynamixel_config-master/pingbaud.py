#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Cleber de Souza Couto Filho
import os
import time

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

# Baudrates list
BAUDRATES                    = [1000000,500000,400000,250000,200000,115200,57600,19200,9600]
# Check which port is being used on your controller
DEVICENAME                  = "/dev/ttyUSB0".encode('utf-8')
                                                            # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0"
# Communication Success result value
COMM_SUCCESS                = 0
# Communication Tx Failed
COMM_TX_FAIL                = -1001

# Initialize PortHandler Structs
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
port_num = dynamixel.portHandler(DEVICENAME)

# Initialize PacketHandler Structs
dynamixel.packetHandler()

# Communication result
dxl_comm_result = COMM_TX_FAIL
#ID range request
init = raw_input("Input the ID you want to start to ping:")
try:
    init = int(init)
except ValueError:
    print("Invalid number")

y = raw_input("Input the ID you want to stop:")
try:
    y = int(y)
except ValueError:
    print("Invalid number")

# Open port
if dynamixel.openPort(port_num):
    print("Succeeded to open the port!")
else:
    print("Failed to open the port!")
    print("Press any key to terminate...")
    getch()
    quit()

#Found servos dictionary
found_servos = {}

for i in BAUDRATES:

    # Set port baudrate
    if dynamixel.setBaudRate(port_num, i):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        print("Press any key to terminate...")
        getch()
        quit()
    time.sleep(0.2)
    DXL_ID  = init
    while DXL_ID <= y:
        print("Pinging in ID: %s " % DXL_ID)
        # Try to ping the Dynamixel
        # Get Dynamixel model number
        dxl_model_number = dynamixel.pingGetModelNum(port_num, PROTOCOL_VERSION, DXL_ID)
        if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION) != COMM_SUCCESS:
            dynamixel.printTxRxResult(PROTOCOL_VERSION, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION))
        elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION) != 0:
            dynamixel.printRxPacketError(PROTOCOL_VERSION, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION))
        else:
            print("[ID:%03d] ping Succeeded. Dynamixel model number : %d" % (DXL_ID, dxl_model_number))
            found_servos[DXL_ID] = i

        DXL_ID = DXL_ID + 1

if len(found_servos) == 0:
    print("Nothing was found")
else:
print("These are the servos in the network:"),
for j in found_servos:
    print('ID:%s with baud rate: %s,' % (j , found_servos[j]))

# Close port
dynamixel.closePort(port_num)
