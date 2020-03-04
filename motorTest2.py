import  RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

mB=GPIO.PWM(7,100)
mB.start(0)


mF=GPIO.PWM(13,100)
mF.start(0)

GPIO.setup(11,GPIO.OUT,initial=1)
GPIO.setup(12,GPIO.OUT,initial=0)
GPIO.setup(15,GPIO.OUT,initial=1)
GPIO.setup(16,GPIO.OUT,initial=0)



for PWMSpd in range(0,101,10):
    print(PWMSpd)
    mB.ChangeDutyCycle(PWMSpd)
#    m2.ChangeDutyCycle(PWMSpd)
    sleep(3)
for PWMSpd in range(100,-1,-10):
    mB1.ChangeDutyCycle(PWMSpd)
#    m2.ChangeDutyCycle(PWMSpd)
    sleep(3)
m1.ChangeDutyCycle(20)
m2.ChangeDutyCycle(0)
sleep(3)
GPIO.output(11,GPIO.LOW)
GPIO.output(12,GPIO.HIGH)

sleep(3)
m1.ChangeDutyCycle(0)
m2.ChangeDutyCycle(20)
sleep(3)
GPIO.output(15,GPIO.HIGH)
GPIO.output(16,GPIO.LOW)
sleep(3)






GPIO.cleanup()
