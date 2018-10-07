import time 
import serial

i = 0
temps = []
path = "C:\\example\\"

def getemps() :
    ser = serial.Serial('/dev/ttyACM0',9600)
    i = 0
    ser.flush()
    while i < 10 :
        read_serial=ser.readline()
        temps.append(read_serial)
        i = i+1 

def fillist () :
    print("Informe 10 numeros")
    i = 0
    while i < 10 :
        num = int(input("Numero %i : " %(i+1)))
        temps.append(num)
        i = i+1
        time.sleep(0.5)
         
def media(l): 
    soma = 0
    for e in l :
        soma += e
    return (soma/len(l))

def saveTemps(l,mini,maxi,media) :
    arquivo = open(path,"w")
    arquivo.write("Todas as temperaturas : \n")
    for e in l :
        arquivo.write(str("{0}ºC ").format(e))
        arquivo.write("\n")
    arquivo.write(str("Temperatura minima :{0} \nTemperatura maxima :{1} \nTemperatura media :{2}".format(mini ,maxi ,media)))
    arquivo.close()

def filenamer() :
    timer = time.strftime(".%H%M")
    date = time.strftime("%d%m%y")
    name = str(date+timer)+".txt"
    return name
    
path = path+filenamer()
getemps()
media = (media(temps))   
maxi = max(temps)
mini = min(temps)
saveTemps(temps,mini,maxi,media)



