import serial
import time
ser = serial.Serial('COM4', 9600, timeout=0)
 
while 1:
    comand = input()
    ser.write(comand.encode())
    time.sleep(1/10)
   
    while(ser.inWaiting()>0):
        read = ser.readline().decode()
        print(read)
            
