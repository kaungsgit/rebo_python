"""
Send a number to arduino
"""
# import serial
# 
# ser = serial.Serial('/dev/ttyACM0', 9600)
# 
# # send 3 to arduino, who's running myblink
# # should see arduino LED 13 blinking 3 times
# ser.write(b"7")

"""
Send a string to arduino
"""
#!/usr/bin/env python3
import serial
import time
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        value1 = -8
        value2 = -100
        
        value1 = str(value1).zfill(4)
        value2 = str(value2).zfill(4)
        
        value3 = str(value1)+','+str(value2)
        
        ser.write((value3+'\n').encode())
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(0.1)
        
        
#         ser.write(b"Hello from Raspberry Pi!\n")
#         line = ser.readline().decode('utf-8').rstrip()
#         print(line)
#         time.sleep(1)