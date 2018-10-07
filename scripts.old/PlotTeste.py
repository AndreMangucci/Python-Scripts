import matplotlib.pyplot as plt

n = int(input("Tamanho do intervalo"))
x = []
y = []

for i in range(n):
	x.append(input("Digite um numero : "))
for i in range(n):
	y.append(input("Digite um numero : "))
print(x,y)
xmax = int(max(x))
ymax = int(max(y))


plt.plot(x, y)
plt.axis([0, xmax, 0, ymax])
plt.grid(True)
plt.ylabel("Eixo Y")
plt.ylabel("Eixo X")
plt.show()
