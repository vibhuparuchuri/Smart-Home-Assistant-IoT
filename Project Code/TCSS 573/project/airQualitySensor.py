import time
import grovepi
 
# Connect the Grove Air Quality Sensor to analog port A0
# SIG,NC,VCC,GND
air_sensor = 1
 
grovepi.pinMode(air_sensor,"INPUT")
 
while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(air_sensor)
        
        if sensor_value > 0:
		print sensor_value
        time.sleep(3)
 
    except IOError:
        print "Error"
