def generate_sum_of_numbers(start, end):
    numbers = range(start, end + 1)
    sum_of_numbers = sum(numbers)

    print(f"La suma de todos los números entre {start} y {end} es: {sum_of_numbers}")

def main():
    start = int(input("Ingrese el primer número: "))
    end = int(input("Ingrese el segundo número: "))

    if start > end:
        print("El primer número no puede ser mayor que el segundo número.")
    else:
        generate_sum_of_numbers(start, end)

if __name__ == "__main__":
    main()