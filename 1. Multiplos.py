def show_multiplication_table(number):
    print(f"Tabla de multiplicar del {number}:")

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

def main():
    number = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    show_multiplication_table(number)

if __name__ == "__main__":
    main()