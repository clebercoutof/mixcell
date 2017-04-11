#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Class containing the dynamixel info
class Dynamixel:
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
DEVICENAME                   = "/dev/ttyUSB0".encode('utf-8')# Check which port is being used on your controller
PROTOCOL_1                   = 1                                                            # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0"


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

OPERATION_MODE = 0x00 # Mode is unavailable in Protocol 1.0 Reset
model_num = {44:"AX-12W",18:"AX-12A",28:"EX-106+",24:"RX-24F",28:"RX-28",64:"RX-64",104:"MX-12W",29:"MX-28",54:"MX-64",320:"MX-106"}

# Communication result
dxl_comm_result = COMM_TX_FAIL                            

def search(id_search_min, id_search_max, baudrates_search_list):
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
        print("Press any key to terminate...")
        getch()
        quit()

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
                print("Press any key to terminate...")
                getch()
                quit()
        
                time.sleep(0.2)
            
            while actual_id <= end:            
                print("Pinging in ID: %s " % actual_id)
                # Try to ping the Dynamixel
                # Get Dynamixel model number
                dxl_model_number = dynamixel.pingGetModelNum(port_num, protocol, actual_id)
                if dynamixel.getLastTxRxResult(port_num, protocol) != COMM_SUCCESS:
                    dynamixel.printTxRxResult(protocol, dynamixel.getLastTxRxResult(port_num, protocol))
                        
                elif dynamixel.getLastRxPacketError(port_num, protocol) != 0:
                    dynamixel.printRxPacketError(protocol, dynamixel.getLastRxPacketError(port_num, protocol))
                        
                else:
                    #Case the ping succeeds, creates an servo object and stores it in the found_servos vector
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
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        print("Press any key to terminate...")
        getch()
        quit()    
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        print("Press any key to terminate...")
        getch()
        quit()    
    #Write CW angle limit
    dynamixel.write2ByteTxRx(port_num, PROTOCOL_1 , id, ADDR_CW_ANGLE_LIMIT, cw_angle_limit)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_1 , dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1 , dynamixel.getLastRxPacketError(port_num,PROTOCOL_1 ))
        return 0
    else:
        print("CW angle changed to: %s" % cw_angle_limit)
        time.sleep(0.5)
   
    # Write CCW angle limit
    dynamixel.write2ByteTxRx(port_num, PROTOCOL_1 , id, ADDR_CCW_ANGLE_LIMIT, ccw_angle_limit)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_1 , dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1 , dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ))
        return 0
    else:
        print("CCW angle changed to: %s" % ccw_angle_limit)
        time.sleep(0.5)
        
def factory_reset(id,baudrate):
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        print("Press any key to terminate...")
        getch()
        quit()    
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        print("Press any key to terminate...")
        getch()
        quit()
        
    dynamixel.factoryReset(port_num, PROTOCOL_1 , id, OPERATION_MODE)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ) != COMM_SUCCESS:
        print("Aborted")
        dynamixel.printTxRxResult(PROTOCOL_1 , dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1 , dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ))  
        # Wait for reset
        sleep(2)
        return 1
    
def set_torque_max(id, percentage,baudrate):
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        print("Press any key to terminate...")
        getch()
        quit()    
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        print("Press any key to terminate...")
        getch()
        quit()
    #Converting percentage to bit value (check dynamixel e-manual for info)    
    if percentage == 100:
        value = 1023
    else:
        value = int(percentage/0.0977517107)
    #Writing the value in the address
    dynamixel.write2ByteTxRx(port_num, PROTOCOL_1 , id, ADDR_MAX_TORQUE, value)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_1 , dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1 , dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ))
        return 0
    else:
        time.sleep(0.2)
        return 1

def set_id(id, new_id,baudrate):
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        print("Press any key to terminate...")
        getch()
        quit()    
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        print("Press any key to terminate...")
        getch()
        quit()        
    #Writes the new ID onto the register    
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1 ,id, ADDR_ID, new_id)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_1, dynamixel.getLastTxRxResult(port_num, PROTOCOL_1))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1, dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ))
        return 0
    else:
    #ID CHANGED
        time.sleep(0.2)
        return 1
        
def set_baudrate(id,new_baudrate,baudrate):
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        print("Press any key to terminate...")
        getch()
        quit()    
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        print("Press any key to terminate...")
        getch()
        quit()
        
    baudnum = {1000000:1,500000:3,400000:4,250000:7 , 200000 :9 , 115200 : 16 , 57600 : 34 , 19200 : 103 , 9600 : 207}
    value = baudnum[new_baudrate]
    
    # Set baudrate
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1 , id, ADDR_BAUDRATE, value)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_1 , dynamixel.getLastTxRxResult(port_num, PROTOCOL_1 ))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1 , dynamixel.getLastRxPacketError(port_num, PROTOCOL_1 ))
        return 0
    else:
        #BAUDRATE CHANGED
        time.sleep(0.2)
        return 1


def reverse_slave(id,reverse_mode_enable,slave_mode_enable,baudrate):
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        print("Press any key to terminate...")
        getch()
        quit()    
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        print("Press any key to terminate...")
        getch()
        quit()
        
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
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_1, dynamixel.getLastTxRxResult(port_num, PROTOCOL_1))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1, dynamixel.getLastRxPacketError(port_num, PROTOCOL_1))
        return 0
    else:
        print("Drive mode changed")
        time.sleep(0.2)

def set_pid_gain(id,dgain,igain,pgain,baudrate):
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    port_num = dynamixel.portHandler(DEVICENAME)
    # Initialize PacketHandler Structs
    dynamixel.packetHandler()
    # Open port
    if dynamixel.openPort(port_num):
        print("Succeeded to open the port!")
    else:
        print("Failed to open the port!")
        print("Press any key to terminate...")
        getch()
        quit()    
    # Set port baudrate
    if dynamixel.setBaudRate(port_num, baudrate):
        print("Succeeded to change the baudrate!")
    else:
        print("Failed to change the baudrate!")
        print("Press any key to terminate...")
        getch()
        quit()        
    # D gain config
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1, id, ADDR_D_GAIN, dgain)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_1, dynamixel.getLastTxRxResult(port_num, PROTOCOL_1))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1, dynamixel.getLastRxPacketError(port_num, PROTOCOL_1))
        return 0
    else:
        #D gain set
        time.sleep(0.5)

    
    # I gain config
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1, id, ADDR_I_GAIN, igain)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_1, dynamixel.getLastTxRxResult(port_num, PROTOCOL_1))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1, dynamixel.getLastRxPacketError(port_num, PROTOCOL_1))
        return 0
    else:
        #I gain set
        time.sleep(0.5)

    
    # P gain config
    dynamixel.write1ByteTxRx(port_num, PROTOCOL_1, id, ADDR_P_GAIN, pgain)
    if dynamixel.getLastTxRxResult(port_num, PROTOCOL_1) != COMM_SUCCESS:
        dynamixel.printTxRxResult(PROTOCOL_1, dynamixel.getLastTxRxResult(port_num, PROTOCOL_1))
        return 0
    elif dynamixel.getLastRxPacketError(port_num, PROTOCOL_1) != 0:
        dynamixel.printRxPacketError(PROTOCOL_1, dynamixel.getLastRxPacketError(port_num, PROTOCOL_1))
        return 0
    else:
        #P gain set
        time.sleep(0.5) 
    
   
    
    
    
