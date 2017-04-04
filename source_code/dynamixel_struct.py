#Class containing the dynamixel info
class Dynamixel:
    def __init__(self):
        self.id = 0
        self.baudrate = 0
        self.protocol = 1
        self.model = ""
    
def servo_scan():
    x = input("servos number")
    found_servos = []
    for i in range(x):
        i = Dynamixel()
        i.id = input("input id")
        i.model = input("input model")
        i.baudrate = input("input baudrate")
       
        found_servos.append(i)

    return found_servos         