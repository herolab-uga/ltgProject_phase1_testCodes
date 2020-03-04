from motorControl import MotorControl as MC
import getch
MovCnt=MC()

while 1:
	ctl=getch.getch()
	if(ctl=='w'):
		MovCnt.MoveForward()
	elif(ctl=='s'):
		MovCnt.MoveBackward()
	elif(ctl=='q'):
		MovCnt.Stopper()
	elif(ctl=='a'):
		MovCnt.MoveLeft()
	elif(ctl=='d'):
		MovCnt.MoveRight()
