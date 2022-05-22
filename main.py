from motor import Motor
import ps4_controller as js
import time

motor1 = Motor(4, 2, 3, 'm1')
motor2 = Motor(22, 17, 27, 'm2')
motor3 = Motor(11, 10, 9, 'm3')
motor4 = Motor(0, 5, 6, 'm4')


def main():
    
    ps4_output = js.getJS()
    
#     if ps4_output['x'] == 1:
#         motor1.move(-(ps4_output['axis2']), 0.1)
#     if ps4_output['o'] == 1:
#         motor2.move(-(ps4_output['axis2']), 0.1)
#     if ps4_output['t'] == 1:
#         motor3.move(-(ps4_output['axis2']), 0.1)
#     if ps4_output['s'] == 1:
#         motor4.move(-(ps4_output['axis2']), 0.1)
    
    vy = -(ps4_output['axis2'])
    vx = (ps4_output['axis1'])
#     
    motor1.move((vy-vx), 0.1)
    motor2.move((vy+vx), 0.1)
    motor3.move((vy-vx), 0.1)
    motor4.move((vy+vx), 0.1)
#     print(vx, vy)
    
    if ps4_output['share'] == 1:
        motor1.stop()
        motor2.stop()
        motor3.stop()
        motor4.stop()
            
#     print(ps4_output)
    time.sleep(0.05)
    
    
if __name__ == '__main__':
    while True:
        main()
