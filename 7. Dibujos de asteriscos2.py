def triangulo_dibujo(altura):
    for i in range(1, altura + 1):
        print('*' * i)
def main():
    try:
        altura = int(input("Altura: "))      
        if altura > 0:
            triangulo_dibujo(altura)
        else:
            print("INgrese un valor mayor de cero")
    except ValueError:
             print("Ingrese un valor numerico")
if __name__ == "__main__":
     main()
