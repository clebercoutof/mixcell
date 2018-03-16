#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Cleber de Souza Couto Filho (clebercoutof@gmail.com)
#Class containing the dynamixel info
class Dynamixel:
    """This class is used to store the Dynamixel, ``id``, ``baudrate``, ``protocol`` and ``model``."""
  
    def __init__(self):
        self.id = 0
        self.baudrate = 0
        self.protocol = 1
        self.model = ""

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

import dynamixel_functions as dynamixel                     # Uses Dynamixel SDK library

#Search parameters                           
PROTOCOL_VERSIONS           = [1,2]

# Default setting
DEVICENAME                   = "/dev/ttyUSB0".encode('utf-8')
PROTOCOL_1                   = 1                                                           
#ADDRESSES 
ADDR_CW_ANGLE_LIMIT         = 6
ADDR_CCW_ANGLE_LIMIT        = 8
ADDR_MAX_TORQUE             = 14
ADDR_ID                     = 3
ADDR_BAUDRATE               = 4
ADDR_DRIVE_MODE             = 10
ADDR_D_GAIN                 = 26
ADDR_I_GAIN                 = 27
ADDR_P_GAIN                 = 28
#General parameters
COMM_SUCCESS                = 0                             # Communication Success result value
COMM_TX_FAIL                = -1001                         # Communication Tx Failed

PORT_ERROR = 1000
BAUDRATE_ERROR = 1001
COMM_ERROR = 1002
HARDWARE_COMM_ERROR = 1003

OPERATION_MODE = 0x00 # Mode is unavailable in Protocol 1.0 Reset
model_num = {44:"AX-12W",18:"AX-12A",28:"EX-106+",24:"RX-24F",28:"RX-28",64:"RX-64",104:"MX-12W",29:"MX-28",54:"MX-64",320:"MX-106"}

# Communication result
dxl_comm_result = COMM_TX_FAIL                            

def search(id_search_min, id_search_max, baudrates_search_list):
    """Search for servos in range of ``id_search_min`` and ``id_search_max`` for all baudrates in ``baudrates_search_list``.

    :param int id_search_min: ID to start searching.
    :param int id_search_max: ID to stop pinging.
    :param list baudrates_search_list: List containing the baudrates that the user want to search.
    :return: ``found_servos`` list containing the servos found.
    :rtype: List containing the ``Dynamixel`` object servos"""
    #SEARCHING IN THE NETWORK
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        return PORT_ERROR

    #Declaring the limits of the search    
    init = id_search_min
    end = id_search_max
    #List containing the found servos in the network
    found_servos = []
    #Tries to ping in protocols 1 and 2
    for protocol in PROTOCOL_VERSIONS:
        print("Using protocol %s" % str(protocol))
    #Loop through all baudrates
        for baudrate in baudrates_search_list:
            actual_id  = init
            # Set port baudrate
            if dynamixel.setBaudRate(port_num, baudrate):
                print("Succeeded to change the baudrate!")
            else:
                print("Failed to change the baudrate!")
                return BAUDRATE_ERROR
        
            time.sleep(0.2)
            
            while actual_id <= end:            
                print("Pinging in ID: %s " % actual_id)
                # Try to ping the Dynamixel
                # Get Dynamixel model number
                dxl_model_number = dynamixel.pingGetModelNum(port_num, protocol, actual_id)
                dxl_comm_result = dynamixel.getLastTxRxResult(port_num, protocol)
                dxl_error = dynamixel.getLastRxPacketError(port_num, protocol)
                if dxl_comm_result != COMM_SUCCESS:
                    print(dynamixel.getTxRxResult(protocol, dxl_comm_result))
                elif dxl_error != 0:
                    print(dynamixel.getRxPacketError(protocol, dxl_error))
                else:
                    print("[ID:%03d] ping Succeeded. Dynamixel model number : %d" % (actual_id, dxl_model_number))
                    servo = Dynamixel()
                    servo.id = actual_id
                    servo.baudrate = baudrate
                    servo.protocol = protocol
                    servo.model = dxl_model_number
                    found_servos.append(servo)
                actual_id = actual_id + 1

    # Close port
    dynamixel.closePort(port_num)
    return found_servos


def set_angle_limit(id,cw_angle_limit, ccw_angle_limit,baudrate):
    """Configure the angle limits of a servo.
    
    :param int id: Servo ``ìd``
    :param int cw_angle_limit: Clockwise angle limit to be configured
    :param int ccw_angle_limit: Counter-clockwise angle limit to be configured
    :param baudrate: Baudrate of the servo to be configured
    :return: 
    --``PORT_ERROR`` case it fails to open the port.
    
    --``BAUDRATE_ERROR`` case it fails to change baudrate.
    
    --``COMM_ERROR`` case there is a communication error.
    
    --``HARDWARE_COMM_ERROR`` case there is a hardware communication error.
    
    --``NONE`` case the operation succeeds."""      
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        return PORT_ERROR
    
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        return BAUDRATE_ERROR
    
    # Write goal position
    dynamixel.write2ByteTxRx(port_num, PROTOCOL_1, id, ADDR_CW_ANGLE_LIMIT, cw_angle_limit)
    dxl_comm_result = dynamixel.getLastTxRxResult(port_num, PROTOCOL_1)
    dxl_error = dynamixel.getLastRxPacketError(port_num, PROTOCOL_1)
    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_1, dxl_comm_result))
        return COMM_ERROR
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_1, dxl_error))
        return HARDWARE_COMM_ERROR
    else:
        print("Cw angle changed to: %s" % cw_angle_limit)

    # Write goal position
    dynamixel.write2ByteTxRx(port_num, PROTOCOL_1, id, ADDR_CCW_ANGLE_LIMIT, ccw_angle_limit)
    dxl_comm_result = dynamixel.getLastTxRxResult(port_num, PROTOCOL_1)
    dxl_error = dynamixel.getLastRxPacketError(port_num, PROTOCOL_1)
    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_1, dxl_comm_result))
        return COMM_ERROR
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_1, dxl_error))
        return HARDWARE_COMM_ERROR
    else:
        print("CCW angle changed to: %s" % cw_angle_limit)

    dynamixel.closePort(port_num)

def factory_reset(id,baudrate):
    """Resets a servo to factory config.
    
    :param int id: Servo ``ìd``
    :param baudrate: Baudrate of the servo to be configured
    :return: 
    --``PORT_ERROR`` case it fails to open the port.
    
    --``BAUDRATE_ERROR`` case it fails to change baudrate.
    
    --``COMM_ERROR`` case there is a communication error.
    
    --``HARDWARE_COMM_ERROR`` case there is a hardware communication error.
    
    --``NONE`` case the operation succeeds."""      
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        return PORT_ERROR   
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        return BAUDRATE_ERROR
        
    dynamixel.factoryReset(port_num, PROTOCOL_1 , id, OPERATION_MODE)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ) != COMM_SUCCESS:
        print("Aborted")
        dynamixel.printTxRxResult(PROTOCOL_1 , dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ))
        return COMM_ERROR
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1 , dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ))  
        return HARDWARE_COMM_ERROR
        # Wait for reset
        time.sleep(2)
    
def set_torque_max(id, percentage,baudrate):
    """Sets a servo max torque.
    
    :param int id: Servo ``ìd``
    :param baudrate: Baudrate of the servo to be configured
    :param int percentage: Torque percentage
    :return: 
    --``PORT_ERROR`` case it fails to open the port.
    
    --``BAUDRATE_ERROR`` case it fails to change baudrate.
    
    --``COMM_ERROR`` case there is a communication error.
    
    --``HARDWARE_COMM_ERROR`` case there is a hardware communication error.
    
    --``NONE`` case the operation succeeds."""      
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        return PORT_ERROR   
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        return BAUDRATE_ERROR
    #Converting percentage to bit value (check dynamixel e-manual for info)    
    if percentage == 100:
        value = 1023
    else:
        value = int(percentage/0.0977517107)

    # Write goal position
    dynamixel.write2ByteTxRx(port_num, PROTOCOL_1, id, ADDR_MAX_TORQUE, value)
    dxl_comm_result = dynamixel.getLastTxRxResult(port_num, PROTOCOL_1)
    dxl_error = dynamixel.getLastRxPacketError(port_num, PROTOCOL_1)
    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_1, dxl_comm_result))
        return COMM_ERROR
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_1, dxl_error))
        return HARDWARE_COMM_ERROR
    else:
        print("Torque set to %s " % percentage)
        time.sleep(0.2)

    dynamixel.closePort(port_num)
def set_id(id, new_id,baudrate):
    """Sets a servo ID.
    
    :param int id: Servo ``ìd``
    :param baudrate: Baudrate of the servo to be configured
    :param int new_id: ``new_id`` to be configured
    :return: 
    --``PORT_ERROR`` case it fails to open the port.
    
    --``BAUDRATE_ERROR`` case it fails to change baudrate.
    
    --``COMM_ERROR`` case there is a communication error.
    
    --``HARDWARE_COMM_ERROR`` case there is a hardware communication error.
    
    --``NONE`` case the operation succeeds."""      
     # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        return PORT_ERROR   
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        return BAUDRATE_ERROR
    #Writes the new ID onto the register
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1, id, ADDR_ID, new_id)
    dxl_comm_result = dynamixel.getLastTxRxResult(port_num, PROTOCOL_1)
    dxl_error = dynamixel.getLastRxPacketError(port_num, PROTOCOL_1)
    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_1, dxl_comm_result))
        return COMM_ERROR
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_1, dxl_error))
        return HARDWARE_COMM_ERROR
    else:
        print("ID changed to: %s" % new_id)
        time.sleep(0.2)    
    dynamixel.closePort(port_num)

def set_baudrate(id,new_baudrate,baudrate):
    """Sets a servo baudrate.
    
    :param int id: Servo ``ìd``
    :param baudrate: Baudrate of the servo to be configured
    :param int new_baudrate: ``new_baudrate`` to be configured
    :return: 
    --``PORT_ERROR`` case it fails to open the port.
    
    --``BAUDRATE_ERROR`` case it fails to change baudrate.
    
    --``COMM_ERROR`` case there is a communication error.
    
    --``HARDWARE_COMM_ERROR`` case there is a hardware communication error.
    
    --``NONE`` case the operation succeeds."""    
     # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        return PORT_ERROR   
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        return BAUDRATE_ERROR
    baudnum = {1000000:1,500000:3,400000:4,250000:7 , 200000 :9 , 115200 : 16 , 57600 : 34 , 19200 : 103 , 9600 : 207}
    value = baudnum[new_baudrate]
    
    # Set baudrate
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1, id, ADDR_BAUDRATE, value)
    dxl_comm_result = dynamixel.getLastTxRxResult(port_num, PROTOCOL_1)
    dxl_error = dynamixel.getLastRxPacketError(port_num, PROTOCOL_1)
    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_1, dxl_comm_result))
        return COMM_ERROR
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_1, dxl_error))
        return HARDWARE_COMM_ERROR
    else:
        print("Baudrate changed to : %s" % baudrate)
        time.sleep(0.2) 

    dynamixel.closePort(port_num)

def reverse_slave(id,reverse_mode_enable,slave_mode_enable,baudrate):
    """Sets the drive mode.
    
    :param int id: Servo ``ìd``
    :param baudrate: Baudrate of the servo to be configured
    :param int reverse_mode_enable: Reverse mode checkbox state
    :param int slave_mode_enable: Slave mode checkbox state
    :return: 
    --``PORT_ERROR`` case it fails to open the port.
    
    --``BAUDRATE_ERROR`` case it fails to change baudrate.
    
    --``COMM_ERROR`` case there is a communication error.
    
    --``HARDWARE_COMM_ERROR`` case there is a hardware communication error.
    
    --``NONE`` case the operation succeeds."""    
     # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        return PORT_ERROR   
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        return BAUDRATE_ERROR
        
    slave_binary = 0x02
    reverse_binary = 0x01
    drive_mode_byte = 0x00
    
    if reverse_mode_enable == 2:
        drive_mode_byte = reverse_binary + drive_mode_byte
    else:
        drive_mode_byte = drive_mode_byte
    
    if slave_mode_enable == 2:
        drive_mode_byte = slave_binary + drive_mode_byte
    else:
        drive_mode_byte = drive_mode_byte
    
    # Set drive mode
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1, id, ADDR_DRIVE_MODE, drive_mode_byte)
    dxl_comm_result = dynamixel.getLastTxRxResult(port_num, PROTOCOL_1)
    dxl_error = dynamixel.getLastRxPacketError(port_num, PROTOCOL_1)
    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_1, dxl_comm_result))
        return COMM_ERROR
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_1, dxl_error))
        return HARDWARE_COMM_ERROR
    else:
        print("Drive mode changed")
        time.sleep(0.2)

    dynamixel.closePort(port_num)

def set_pid_gain(id,d_gain,i_gain,p_gain,baudrate):
    """Sets the PID Gains.
    
    :param int id: Servo ``ìd``
    :param baudrate: Baudrate of the servo to be configured
    :param int d_gain: D Gain
    :param int i_gain: I Gain
    :param int p_gain: P Gain
    :return: 
    --``PORT_ERROR`` case it fails to open the port.
    
    --``BAUDRATE_ERROR`` case it fails to change baudrate.
    
    --``COMM_ERROR`` case there is a communication error.
    
    --``HARDWARE_COMM_ERROR`` case there is a hardware communication error.
    
    --``NONE`` case the operation succeeds."""  
     # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        return PORT_ERROR   
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        return BAUDRATE_ERROR
    # D gain config
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1, id, ADDR_D_GAIN, d_gain)
    dxl_comm_result = dynamixel.getLastTxRxResult(port_num, PROTOCOL_1)
    dxl_error = dynamixel.getLastRxPacketError(port_num, PROTOCOL_1)
    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_1, dxl_comm_result))
        return COMM_ERROR
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_1, dxl_error))
        return HARDWARE_COMM_ERROR
    else:
        print("D gain set")
        time.sleep(0.2)                                                                    
    
    # I gain config
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1, id, ADDR_I_GAIN, i_gain)
    dxl_comm_result = dynamixel.getLastTxRxResult(port_num, PROTOCOL_1)
    dxl_error = dynamixel.getLastRxPacketError(port_num, PROTOCOL_1)
    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_1, dxl_comm_result))
        return COMM_ERROR
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_1, dxl_error))
        return HARDWARE_COMM_ERROR
    else:
        print("I gain set")
        time.sleep(0.2)

    
    # P gain config
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1, id, ADDR_P_GAIN, p_gain)
    dxl_comm_result = dynamixel.getLastTxRxResult(port_num, PROTOCOL_1)
    dxl_error = dynamixel.getLastRxPacketError(port_num, PROTOCOL_1)
    if dxl_comm_result != COMM_SUCCESS:
        print(dynamixel.getTxRxResult(PROTOCOL_1, dxl_comm_result))
        return COMM_ERROR
    elif dxl_error != 0:
        print(dynamixel.getRxPacketError(PROTOCOL_1, dxl_error))
        return HARDWARE_COMM_ERROR
    else:
        print("P gain set")
        time.sleep(0.2)
    
    dynamixel.closePort(port_num)
