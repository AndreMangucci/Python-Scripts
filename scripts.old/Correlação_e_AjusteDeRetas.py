from math import sqrt
import matplotlib.pyplot as plt 

x = []
y = []

inptX = (input('Digite os Valores de X separados por virgula : '))
VlrX = inptX.split(',')

n = (len(VlrX))

def ValoresX(strx) :
	for i in range(n) :
		x.append(float(strx[i]))
	return x   

inptY = (input('Digite os Valores de Y separados por virgula : '))
VlrY = inptY.split(',')

def ValoresY(stry) :
	for i in range(n) :
		y.append(float(stry[i]))
	return y 


x = ValoresX(VlrX)
y = ValoresY(VlrY)

def sumXY(l) :
    soma = 0
    for i in range(len(l)) :
        soma = soma+l[i]
    return soma 


def sumXY2(l) :
    soma = 0
    for i in range(len(l)) :
        soma = soma+(pow(l[i],2))
    return soma 

def xMulty(l,t) :
    mult = 0
    soma = 0
    for i in range(len(l)):
        mult = l[i]*t[i]
        soma = soma+mult
    return soma

nElementos = len(x)
somatorioX = (sumXY(x))
somatorioY = (sumXY(y))
somatorioX2 = (sumXY2(x))
somatorioY2 = (sumXY2(y))
somatorioXY = (xMulty(x,y))

def coef_de_correlacao(n,xy,x,y,x2,y2):
    rsup = (n*xy-x*y)
    rinf = (sqrt(n*x2-(x*x))*sqrt(n*y2-(y*y)))
    global r    
    r = round((rsup/rinf),2)
    relacao = ""
    
    if r <= 1 and r > 0.7 :
        relacao = 'Forte Positiva'
        
    elif r <= 0.7 and r > 0.3 :
        relacao = 'Fraca Positiva'
        
    elif r <= 0.3 and r > -0.3 :
        relacao = 'Sem Relação'    
        
    elif r <= -0.3 and r > -0.7 :
        relacao = 'Fraca Negativa'
        
    elif r <= -0.7 and r > -1 :
        relacao = 'Forte Negativa'
            
    return relacao

def ajuste_de_retas(n,xy,x,y,x2) :
    global a
    global b    

    a = round((((n*xy)-(x*y))/(n*x2-(x*x))),2)
    b = round((((y*x2)-(x*xy))/(n*x2-(x*x))),2)

    retaAjustada = ("y = {0}x+{1}".format(a,b)) 

    return retaAjustada

def pontosy(x,a,b) :
    pontos = []
    for i in range(len(x)) :
       pontos.append(b+(x[i]*a))
    return pontos     

def grafico(x,y) :
    xmax = int(max(x))
    xmin = int(min(x))    
    ymax = int(max(y))    
    ymin = int(min(y))
    
    plt.plot(x, y)
    plt.axis([(xmin-(xmin/5)), (xmax+(xmax/5)), (ymin-(ymin/5)), (ymax+(ymax/5))])
    plt.grid(True)
    plt.ylabel("Eixo Y")
    plt.xlabel("Eixo X")
    plt.show()

print(x,y)       
print(coef_de_correlacao(nElementos,somatorioXY,somatorioX,somatorioY,somatorioX2,somatorioY2))
print(r)
print(ajuste_de_retas(nElementos,somatorioXY,somatorioX,somatorioY,somatorioX2))
grafico(x,(pontosy(x,a,b)))

