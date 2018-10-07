import serial
import time
c = True
ser = serial.Serial('COM5', 9600, timeout=0)

while c == True :
	comand  = "1"
	ser.write(comand.encode())
	if ser.inWaiting():
		resposta = (ser.readline().decode())
		print(resposta)	
		if resposta == '49' :
			print("Stopped")