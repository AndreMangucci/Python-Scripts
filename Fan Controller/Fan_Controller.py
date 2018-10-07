import serial
import time

read = ""
inst = {'adv1':"Selecione o Fan a ser controlado",'adv2':"Fan 1 Selecionado",'adv3':"Digite 1 para ligar\desligar, 2 para o controle de velocidade, 0 para voltar",'adv4':"Saindo...",'adv5':"Ligar e desligar",'adv6':"Digite 0 para desligar 1 para ligar",'adv7':"Controle de velocidade",'adv8':"Digite um valor de 0 - 100",'adv9':"Fan não encontrado "}

ser = serial.Serial('COM3', 9600, timeout=0)

while 1:
  time.sleep(1)
  ser.flush()
  while ser.inWaiting() > 0 :
    read = ser.readline().decode()
    if(len(read)== 8):
      lista = read[0:4],read[4:]
      print (inst[lista[0]])
      print(inst[lista[1]])
    else :
      print (inst[read])
    
  comand = input()  
  ser.write(comand.encode())
  time.sleep(1)
