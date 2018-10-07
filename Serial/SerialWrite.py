import serial
import time

read = ""

ser = serial.Serial('COM4', 9600, timeout=0)
while True:
    print ser.readline()  
