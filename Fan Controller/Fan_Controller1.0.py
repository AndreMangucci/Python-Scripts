import serial
import time
ser = serial.Serial('COM3', 9600, timeout=0)

list1 = ['Selecione o fan \n 1 - CPU \n 2 - Case \n','Selecione a velocidade 0 a 100 \n']

read = ""
c = 0

while 1 :

    print(list1[c])
    c = c+1
    
    command = input()
    ser.write(command.encode())

    if(c > 1) :
        c = 0
