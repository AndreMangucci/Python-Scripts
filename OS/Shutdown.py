import os

timer = 0

while 1 :

    tempo = input("Digite o tempo em minutos hh:mm:ss ou cancel : ")

    if(tempo == "CANCEL" or tempo == "cancel") :
        os.system('shutdown -a')

    else :
        tempo = tempo.split(':')
        tempo = [int(c) for c in tempo]
  
        horas = tempo[:1]
        horas = horas[0]*3600 

        minutos = tempo[1:2]
        minutos = minutos[0]*60

        segundos = tempo[2:]
        segundos = segundos[0]

        timer = horas+minutos+segundos   
            
        os.system('shutdown -s -t {0}'.format(timer))
