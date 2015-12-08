import picamera
from time import sleep

camera = picamera.PiCamera()
try:	
	camera.resolution = (640,480)
	#camera.capture('image.jpg')
	camera.preview_fullscreen = False
	camera.preview_window = (100,100,800,600)
	camera.start_preview()
	
	sleep(60)
	camera.stop_preview()
	pass
finally:
	camera.close()
