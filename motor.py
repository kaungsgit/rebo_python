import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


# in1, in2, ena = 2, 3, 4
#
# GPIO.setup(ena, GPIO.OUT)
# GPIO.setup(in1, GPIO.OUT)
# GPIO.setup(in2, GPIO.OUT)
#
# pwm = GPIO.PWM(ena, 100)
# pwm.start(0)

# # while True:
# GPIO.output(in1, GPIO.LOW)
# GPIO.output(in2, GPIO.HIGH)
#
# pwm.ChangeDutyCycle(50)
#
# sleep(2)
# GPIO.output(in1, GPIO.HIGH)
# GPIO.output(in2, GPIO.LOW)
#
# pwm.ChangeDutyCycle(50)
# sleep(2)
#
# pwm.ChangeDutyCycle(0)


class Motor:
    def __init__(self, ena, in1, in2, name='m1'):
        self.name = name
        self.ena = ena
        self.in1 = in1
        self.in2 = in2

        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)

        self.pwm = GPIO.PWM(self.ena, 100)
        self.pwm.start(0)

    def move_forward(self, speed_pct=50, time_dur=0):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed_pct)
        sleep(time_dur)

    def move_backward(self, speed_pct=50, time_dur=0):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed_pct)
        sleep(time_dur)
        
    def move(self, speed_pct=0.5, time_dur=0):
        speed_pct*=50
        if speed_pct>100: speed_pct=100
        elif speed_pct<-100: speed_pct= -100
        
        if speed_pct > 0:
            GPIO.output(self.in1, GPIO.LOW)
            GPIO.output(self.in2, GPIO.HIGH)
            self.pwm.ChangeDutyCycle(abs(speed_pct))
#             print(f'{self.name} moving forward at {abs(speed_pct)}')
        elif speed_pct < 0:
            GPIO.output(self.in1, GPIO.HIGH)
            GPIO.output(self.in2, GPIO.LOW)
            self.pwm.ChangeDutyCycle(abs(speed_pct))
#             print(f'{self.name} moving backward at {abs(speed_pct)}')
        else:
#             print(f'{self.name} not Moving')
            self.pwm.ChangeDutyCycle(0)
            
        sleep(time_dur)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)

if __name__ == '__main__':

    motor1 = Motor(4, 2, 3)
    motor1.move_forward(100, 4)
    motor1.stop()



