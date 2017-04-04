#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright (c) 2016, ROBOTIS CO., LTD.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of ROBOTIS nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
################################################################################

# Author: Ryu Woon Jung (Leon)

#
# *********     Protocol Combined Example      *********
#
#
# Available Dynamixel model on this example : All models using Protocol 1.0 and 2.0
# This example is tested with a Dynamixel MX-28, a Dynamixel PRO 54-200 and an USB2DYNAMIXEL
# Be sure that properties of Dynamixel MX and PRO are already set as %% MX - ID : 1 / Baudnum : 1 (Baudrate : 1000000) , PRO - ID : 1 / Baudnum : 3 (Baudrate : 1000000)
#

# Be aware that:
# This example configures two different control tables (especially, if it uses Dynamixel and Dynamixel PRO). It may modify critical Dynamixel parameter on the control table, if Dynamixels have wrong ID.
#

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

# Control table address for Dynamixel MX
ADDR_MX_TORQUE_ENABLE       = 24                            # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION       = 30
ADDR_MX_PRESENT_POSITION    = 36

# Control table address for Dynamixel PRO
ADDR_PRO_TORQUE_ENABLE      = 562
ADDR_PRO_GOAL_POSITION      = 596
ADDR_PRO_PRESENT_POSITION   = 611

# Protocol version
PROTOCOL_VERSION1           = 1                             # See which protocol version is used in the Dynamixel
PROTOCOL_VERSION2           = 2

# Default setting
DXL1_ID                     = 1                             # Dynamixel ID: 1
DXL2_ID                     = 2                             # Dynamixel ID: 2
BAUDRATE                    = 1000000
DEVICENAME                  = "/dev/ttyUSB0".encode('utf-8')# Check which port is being used on your controller
                                                            # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0"

TORQUE_ENABLE               = 1                             # Value for enabling the torque
TORQUE_DISABLE              = 0                             # Value for disabling the torque
DXL1_MINIMUM_POSITION_VALUE = 100                           # Dynamixel will rotate between this value
DXL1_MAXIMUM_POSITION_VALUE = 4000                          # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL2_MINIMUM_POSITION_VALUE = -150000
DXL2_MAXIMUM_POSITION_VALUE = 150000
DXL1_MOVING_STATUS_THRESHOLD = 10                           # Dynamixel moving status threshold
DXL2_MOVING_STATUS_THRESHOLD = 20

ESC_ASCII_VALUE             = 0x1b

COMM_SUCCESS                = 0                             # Communication Success result value
COMM_TX_FAIL                = -1001                         # Communication Tx Failed

# Initialize PortHandler Structs
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
port_num = dynamixel.portHandler(DEVICENAME)

# Initialize PacketHandler Structs
dynamixel.packetHandler()

index = 0
dxl_comm_result = COMM_TX_FAIL                              # Communication result
dxl1_goal_position = [DXL1_MINIMUM_POSITION_VALUE, DXL1_MAXIMUM_POSITION_VALUE]         # Goal position of Dynamixel MX
dxl2_goal_position = [DXL2_MINIMUM_POSITION_VALUE, DXL2_MAXIMUM_POSITION_VALUE]         # Goal position of Dynamixel PRO
dxl_error = 0                                               # Dynamixel error
dxl1_present_position = 0                                   # Present position of Dynamixel MX
dxl2_present_position = 0                                   # Present position of Dynamixel PRO

# Open port
if dynamixel.openPort(port_num):
    print("Succeeded to open the port!")
else:
    print("Failed to open the port!")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if dynamixel.setBaudRate(port_num, BAUDRATE):
    print("Succeeded to change the baudrate!")
else:
    print("Failed to change the baudrate!")
    print("Press any key to terminate...")
    getch()
    quit()


# Enable Dynamixel#1 torque
dynamixel.write1ByteTxRx(port_num, PROTOCOL_VERSION1, DXL1_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION1) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION1, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION1))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION1) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION1, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION1))
else:
    print("Dynamixel#%d has been successfully connected" % (DXL1_ID))

# Enable Dynamixel#1 torque
dynamixel.write1ByteTxRx(port_num, PROTOCOL_VERSION2, DXL2_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION2) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION2, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION2))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION2) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION2, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION2))
else:
    print("Dynamixel#%d has been successfully connected" % (DXL2_ID))


while 1:
    print("Press any key to continue! (or press ESC to quit!)")
    if getch() == chr(ESC_ASCII_VALUE):
        break

    # Write Dynamixel#1 goal position
    dynamixel.write2ByteTxRx(port_num, PROTOCOL_VERSION1, DXL1_ID, ADDR_MX_GOAL_POSITION, dxl1_goal_position[index])
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION1) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_VERSION1, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION1))
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION1) != 0:
        dynamixel.printRxPacketError(PROTOCOL_VERSION1, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION1))

    # Write Dynamixel#1 goal position
    dynamixel.write4ByteTxRx(port_num, PROTOCOL_VERSION2, DXL2_ID, ADDR_PRO_GOAL_POSITION, dxl2_goal_position[index])
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION2) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_VERSION2, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION2))
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION2) != 0:
        dynamixel.printRxPacketError(PROTOCOL_VERSION2, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION2))

    while 1:
        # Read Dynamixel#1 present position
        dxl1_present_position = dynamixel.read2ByteTxRx(port_num, PROTOCOL_VERSION1, DXL1_ID, ADDR_MX_PRESENT_POSITION)
        if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION1) != COMM_SUCCESS:
            dynamixel.printTxRxResult(PROTOCOL_VERSION1, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION1))
        elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION1) != 0:
            dynamixel.printRxPacketError(PROTOCOL_VERSION1, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION1))

        # Read Dynamixel#2 present position
        dxl2_present_position = dynamixel.read4ByteTxRx(port_num, PROTOCOL_VERSION2, DXL2_ID, ADDR_PRO_PRESENT_POSITION)
        if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION2) != COMM_SUCCESS:
            dynamixel.printTxRxResult(PROTOCOL_VERSION2, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION2))
        elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION2) != 0:
            dynamixel.printRxPacketError(PROTOCOL_VERSION2, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION2))


        print("[ID:%03d] GoalPos:%03d  PresPos:%03d [ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL1_ID, dxl1_goal_position[index], dxl1_present_position, DXL2_ID, dxl2_goal_position[index], dxl2_present_position))

        if not ((abs(dxl1_goal_position[index] - dxl1_present_position) > DXL1_MOVING_STATUS_THRESHOLD) or (abs(dxl2_goal_position[index] - dxl2_present_position) > DXL2_MOVING_STATUS_THRESHOLD)):
            break

    # Change goal position
    if index == 0:
        index = 1
    else:
        index = 0


# Disable Dynamixel#1 Torque
dynamixel.write1ByteTxRx(port_num, PROTOCOL_VERSION1, DXL1_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION1) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION1, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION1))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION1) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION1, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION1))

# Disable Dynamixel#2 Torque
dynamixel.write1ByteTxRx(port_num, PROTOCOL_VERSION2, DXL2_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
if dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION2) != COMM_SUCCESS:
    dynamixel.printTxRxResult(PROTOCOL_VERSION2, dynamixel.getLastTxRxResult(port_num, PROTOCOL_VERSION2))
elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION2) != 0:
    dynamixel.printRxPacketError(PROTOCOL_VERSION2, dynamixel.getLastRxPacketError(port_num, PROTOCOL_VERSION2))


# Close port
dynamixel.closePort(port_num)
