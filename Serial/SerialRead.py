import serial
import time

w = 0
ser = serial.Serial('COM4', 9600, timeout=0)

while(ser.inWaiting()<0):
    read = ser.read(10).decode('cp1252')
if(ser.inWaiting()>0):    
    print(read)

#while 1 :
 #   comand = input("Digite um comando")  
  #  ser.write(comand.encode()) 
   # if(ser.inWaiting()>0):
    #    read = ser.read(10).decode('cp1252')
      
  





