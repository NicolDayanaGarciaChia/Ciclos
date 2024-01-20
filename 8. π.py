numero = int(input('n: '))
suma = 0
for i in range(numero):
    suma+=(-1)**(i)*(1/(2*i+1))
pi = 4 * suma
print(pi)
