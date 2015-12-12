from time import sleep
import RPi.GPIO as GPIO
import sys
import picamera
#Moves motors
def move(p_umdrehung, p_r,p_l,p_direction):
	try:
		GPIO.setmode(GPIO.BCM)

		#Verwendete Pin am Raspberry Pi
		StepPinsR = [18,23,24,25]
		StepPinsL = [12,16,20,21] 
		print "Setup pins left"
		for pin in StepPinsL:	
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin, False)
		print "Setup pins right"
		for pin in StepPinsR:
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin, False)

		Seq = [[1,0,0,1],
			   [1,0,0,0],
			   [1,1,0,0],
			   [0,1,0,0],
			   [0,1,1,0],
			   [0,0,1,0],
			   [0,0,1,1],
			   [0,0,0,1]]

		StepCount = len(Seq)

		WaitTime = 0.005

		StepCounter = 0

		#Umdrehung
		r=p_umdrehung
		#if len(sys.argv)>1:
		#	r = int(sys.argv[1])
		#else:
		#	r = 512

		#Wheels
		L = p_l
		R = p_r
		#if len(sys.argv)>2:
		#	L = int(sys.argv[2])
		#if len(sys.argv)>3:
		#	R = int(sys.argv[3])

		#set 1 for clockwise
		#set -1 for counter-clockwise
		StepDir = p_direction
		#if len(sys.argv)>4:
		#	tmpStepDir = sys.argv[4]
		#	if (tmpStepDir=="L" or tmpStepDir=="l"):
		#		StepDir = -1
		#	else:
		#		StepDir = 1
				
		for s in range (5):	
			for i in range (r):
				print StepCounter
				print Seq[StepCounter]
				
				for pin in range(0,4):
					Lpin = StepPinsL[pin] 
					Rpin = StepPinsR[pin] 
					if Seq[StepCounter][pin]!=0:
						if (L==1):
							print " Enable GPIO %i for Left" %(Lpin)
							GPIO.output(Lpin,True)
						if (R==1):
							print " Enable GPIO %i for Right" %(Rpin)
							GPIO.output(Rpin,True)
					else:
						if (L==1):
							GPIO.output(Lpin,False)
						if (R==1):
							GPIO.output(Rpin,False)
						
				StepCounter += StepDir
				
				if (StepCounter>=StepCount):
					StepCounter = 0
				if (StepCounter<0):
					StepCounter = StepCount + StepDir
				
				#camera.capture('image.jpg')
				sleep(WaitTime)
			#sleep(2)
		#Wait before turning of the camera
		#sleep(5)
		#camera.stop_preview()
		return
		pass
	finally:
		GPIO.cleanup()

#Program to Capture a sequence of images		
def program1(p_seq):
	try:
		camera.resolution = (640,480)
		camera.preview_fullscreen = False
		camera.preview_window = (500,330,500,400)
		camera.start_preview()	
		sleep(2)
	
		for i in range (p_seq):
			#correct smaller wheel
			move(10,0,1,1)
			#Move one pic
			move(25,1,1,1)
			#correct smaller wheel
			move(2,0,1,1)
			#capture image
			#camera.capture('image.jpg')
			sleep(2)
			
		#Wait before turning of the camera	
		#sleep(2)
		camera.stop_preview()
		return

#program that turns both wheels in given direction
def program2(p_seq,p_dir):
	for i in range (p_seq):
		#correct smaller wheel
		move(20,1,1,p_dir)
	return
	
#program that turns left wheel in given direction
def program3(p_seq,p_dir):
	for i in range (p_seq):
		move(20,1,0,p_dir)
	return
	
#program that turns right wheel in given direction
def program4(p_seq,p_dir):
	for i in range (p_seq):
		move(20,0,1,p_dir)
	return
	
camera = picamera.PiCamera()
	
try:	
	p = 0
	if len(sys.argv)>1:
		p = int(sys.argv[1])
	
	s = 1
	if len(sys.argv)>2:
		s = int(sys.argv[2])
		
	d = 1
	if len(sys.argv)>3:
		d = int(sys.argv[3])	
	
	if p = 1:
		program1(s)
	elif p=2:
		program2(s,d)
	elif p=3:
		program3(s,d)
	elif p=4:
		program3(s,d)
	else:
		print "No programm selected. Try  sudo python moto1.py 1"

	pass
finally:
	camera.close()
	#GPIO.cleanup()
