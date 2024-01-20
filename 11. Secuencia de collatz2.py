numero = int(input('n: '))
j=0
for i in range(1,numero+1):
    j=i
    len=1
    while j!=1:
        len+=1
        if j%2==0:
            j /= 2
        else:
            j = j*3+1
    salida_fila = len * '*'
    print(f'{i} {salida_fila}')
     