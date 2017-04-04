found_servos = {1:'a'}

if len(found_servos) == 0:
    print("Nothing was found")
for j in found_servos:


    print('ID:%s with baud rate: %s,' % (j , found_servos[j]))
