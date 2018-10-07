import serial
import time
ser = serial.Serial('COM4', 9600, timeout=0)

while 1 :

    command = input("Digite a : ")
    ser.write(command.encode())
    time.sleep(1/10)
    
    while ser.inWaiting():
        print (ser.readline().decode())
    

