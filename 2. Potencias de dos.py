def generate_powers_of_two(power):
    number = 0
    result = number ** power

    print(f"Las {power}-ésimas potencias de 2 son:")
    for i in range(power + 1):
        print(f"2 ^ {i} = {result}")
        result //= number

def main():
    power = int(input("Ingrese una potencia para ver sus potencias de 2: "))
    generate_powers_of_two(power)

if __name__ == "__main__":
    main()