from motor import Motor
import ps4_controller as js
import time
import serial

def main():
    
    ps4_output = js.getJS()
    
    vy = int(-(ps4_output['axis2'])*100)
    vx = int((ps4_output['axis1'])*100)
    
    turn = int(-(ps4_output['axis3'])*100)
    
    all_forward = int((ps4_output['x'])*100)
#     right = int(-(ps4_output['axis3'])*100)
    
#     print(vx, vy)
    
    start_marker = ''
    end_marker = '\n'
    
    value1 = str(vy).zfill(4)
    value2 = str(vx).zfill(4)
    turn1 = str(turn).zfill(4)
    all_forward1 = str(all_forward).zfill(4)
    
    value3 = value1 + ','+ value2 + ',' + turn1 + ',' + all_forward1
    
    ser.write((start_marker + value3 + end_marker).encode())
    
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    
#     if line != '': # why arduino sends back empty string, no clue...  
#         if line[0] == 'M':
#             print(line)
            
#     time.sleep(0.5)
    
    
    time.sleep(0.05)
    
    
if __name__ == '__main__':
    
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.flush()
    while True:
        main()

