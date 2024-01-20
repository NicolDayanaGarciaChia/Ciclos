def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    num = int(input("Ingrese un número entero: "))
    divisors = get_divisors(num)
    print(f"Los divisores de {num} son: {divisors}")

if __name__ == "__main__":
    main()