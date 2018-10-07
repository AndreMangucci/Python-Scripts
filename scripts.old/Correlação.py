from math import sqrt

x = [i for i in range(3,25,3)]
y = [0,1,2,4,3,5,6,4]

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
    r = round((rsup/rinf),2)
    relacao = ""
    
    if r <= 1 or r >= 0.7 :
        relacao = 'Forte Positiva'
        
    elif r < 0.7 or r >= 0.3 :
        relacao = 'Fraca Positiva'
        
    elif r < 0.3 or r >= -0.3 :
        relacao = 'Sem Relação'    
        
    elif r <= -0.3 or r > -0.7 :
        relacao = 'Forte Negativa'
        
    elif r <= -0.7 or r >= -1 :
        relacao = 'Fraca Negativa'
            
    return relacao

def ajuste_de_retas(n,xy,x,y,x2) :

    a = round((((n*xy)-(x*y))/(n*x2-(x*x))),2)
    b = round((((y*x2)-(x*xy))/(n*x2-(x*x))),2)

    reta = ("y = {0}x+{1}".format(a,b)) 

    return reta

#procurar matplotlib 

print(ajuste_de_retas(nElementos,somatorioXY,somatorioX,somatorioY,somatorioX2))
print(coef_de_correlacao(nElementos,somatorioXY,somatorioX,somatorioY,somatorioX2,somatorioY2))

