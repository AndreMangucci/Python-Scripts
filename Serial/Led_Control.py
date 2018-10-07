import serial
import time

ser = serial.Serial('COM3', 9600, timeout=0)

while 1:
  comand  = input("Digite um comando sendo 1 para ligar e zero desligar : ")
  ser.write(comand.encode())
