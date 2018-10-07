import serial
import time
ser = serial.Serial('COM4', 9600, timeout=0)

read = ""

while 1 :
    
    while ser.inWaiting():
        print (ser.readline().decode())

    
