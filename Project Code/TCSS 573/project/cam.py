from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
print("Taking Picture")
str1 = "/home/pi/Desktop/image5.jpg"
sleep(10)
camera.capture(str1)
camera.stop_preview()
