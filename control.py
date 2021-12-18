import RPi.GPIO as GPIO
import socket
import csv

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)

GPIO.output(29,True)
GPIO.output(31,True)

UDP_IP = "0.0.0.0"
UDP_PORT = 5050

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    raw=data
 
if raw=="forward":
    GPIO.output(11,False)
    GPIO.output(13,True)
    GPIO.output(15,False)
    GPIO.output(33,True)
    print("Robot Move Forward")
   
elif raw=="stop":
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,False)
    GPIO.output(33,False)
    print("Robot Stop")

elif raw=="backward":
    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(15,True)
    GPIO.output(33,False)
    print("Robot Move Backward")

elif raw=="left":
    GPIO.output(11,True)
    GPIO.output(13,True)
    GPIO.output(15,False)
    GPIO.output(33,False)	
    print("Robot Move Left")

elif raw=="right":
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,True)
    GPIO.output(33,True)	
    print("Robot Move Right")

else:
    print("ERROR")
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,False)
    GPIO.output(33,False)
