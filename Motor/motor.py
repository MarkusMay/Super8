from time import sleep
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

#Verwendete Pin am Raspberry Pi
StepPinsL = [18,23,24,25]
StepPinsR = [12,16,20,21] 
for pin in StepPinsL
	print "Setup pins left"
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, False)
for pin in StepPinsR
	print "Setup pins right"
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
#set 1 for clockwise
#set -1 for counter-clockwise
StepDir = 1

WaitTime = 0.005

StepCounter = 0
while True:
	print StepCounter
	print Seq[StepCounter]
	
	for pin in range(0,4)
		xpin = StepPinsL[pin] if Seq[StepCounter][pin]!=0:
			print " Enable GPIO %i" %(xpin)
			GPIO.output(xpin,True)
		else:
			GPIO.output(xpin,False)
	StepCounter += StepDir
	
	if (StepCounter>=StepCount):
		StepCount = 0
	if (StepCounter<0):
		StepCounter = StepCount + StepDir
	
	sleep(WaitTime)
#A=18
#B=23
#C=24
#D=25

#E=12
#F=16
#G=20
#H=21
#time = 0.005

#GPIO.setup(A,GPIO.OUT)
#GPIO.setup(B,GPIO.OUT)
#GPIO.setup(C,GPIO.OUT)
#GPIO.setup(D,GPIO.OUT)
#GPIO.output(A, False)
#GPIO.output(B, False)
#GPIO.output(C, False)
#GPIO.output(D, False)

#GPIO.setup(E,GPIO.OUT)
#GPIO.setup(F,GPIO.OUT)
#GPIO.setup(G,GPIO.OUT)
#GPIO.setup(H,GPIO.OUT)
#GPIO.output(E, False)
#GPIO.output(F, False)
#GPIO.output(G, False)
#GPIO.output(H, False)

X=True
Y=True

#Schritte 1-8- festlegen
def Step1():
	if (X==True):
		GPIO.output(D,True)
	if (Y==True):
		GPIO.output(H,True)
	sleep(time)
	if (X==True):
		GPIO.output(D,False)
	if (Y==True):
		GPIO.output(H,False)
		
def Step2():
	if (X==True):
		GPIO.output(D,True)
		GPIO.output(C,True)
	if (Y==True):
		GPIO.output(H,True)
		GPIO.output(G,True)
	sleep(time)
	if (X==True):
		GPIO.output(D,False)
		GPIO.output(C,False)
	if (Y==True):
		GPIO.output(H,False)
		GPIO.output(G,False)
	
def Step3():
	if (X==True):
		GPIO.output(C,True)
	if (Y==True):
		GPIO.output(G,True)
	sleep(time)
	if (X==True):
		GPIO.output(C,False)
	if (Y==True):
		GPIO.output(G,False)
	
def Step4():
	if (X==True):
		GPIO.output(B,True)
		GPIO.output(C,True)
	if (Y==True):
		GPIO.output(F,True)
		GPIO.output(G,True)
	sleep(time)
	if (X==True):
		GPIO.output(B,False)
		GPIO.output(C,False)
	if (Y==True):
		GPIO.output(F,False)
		GPIO.output(G,False)
	
def Step5():
	if (X==True):
		GPIO.output(B,True)
	if (Y==True):
		GPIO.output(F,True)
	sleep(time)
	if (X==True):
		GPIO.output(B,False)
	if (Y==True):
		GPIO.output(F,False)
	
def Step6():
	if (X==True):
		GPIO.output(A,True)
		GPIO.output(B,True)
	if (Y==True):
		GPIO.output(E,True)
		GPIO.output(F,True)
	sleep(time)
	if (X==True):
		GPIO.output(A,False)
		GPIO.output(B,False)
	if (Y==True):
		GPIO.output(E,False)
		GPIO.output(F,False)
	
def Step7():
	if (X==True):
		GPIO.output(A,True)
		GPIO.output(E,True)
	sleep(time)
	if (X==True):
		GPIO.output(A,False)
		GPIO.output(E,False)
	
def Step8():
	if (X==True):
		GPIO.output(D,True)
		GPIO.output(A,True)
	if (Y==True):
		GPIO.output(H,True)
		GPIO.output(E,True)
	sleep(time)
	if (X==True):
		GPIO.output(D,False)
		GPIO.output(A,False)
	if (Y==True):
		GPIO.output(H,False)
		GPIO.output(E,False)
		
#Umdrehung
r=512
eingabe = raw_input("Steps eingeben:")		
r=int(eingabe)

# Volle Umderehung
for i in range (r):
	Step1()
	Step2()
	Step3()
	Step4()
	Step5()
	Step6()
	Step7()
	Step8()
	
	#Step8()
	#Step7()
	#Step6()
	#Step5()
	#Step4()
	#Step3()
	#Step2()
	#Step1()
	print i
	
GPIO.cleanup()
