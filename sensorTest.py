import RPi.GPIO as GPIO
from motorControl import MotorControl as MC
GPIO.setmode(GPIO.BOARD)
MovCnt=MC()

GPIO.setup(31,GPIO.IN)
GPIO.setup(33,GPIO.IN)
GPIO.setup(35,GPIO.IN)

while 1:
	s3=GPIO.input(31)
	s2=GPIO.input(33)
	s1=GPIO.input(35)
	if(s2==0):
		print('Forward')
		MovCnt.MoveForward()
	elif(s1==0):
		print('Turn Left')
		MovCnt.MoveLeft()
	elif(s3==0):
		print('Turn Right')
		MovCnt.MoveRight()
	else:
		print('Stop')
		MovCnt.Stopper()
	#print('| '+str(s1)+','+str(s2)+','+str(s3)+'|')
