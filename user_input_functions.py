def print_square():
    n = float(input("Введите число: "))
    square = n ** 2
    print(f"Квадрат числа {n} равен {square}")


def check_even_odd():
    n = int(input("Введите число:"))
    if n % 2 == 0:
        print(f"Число {n} является четным.")
    else:
        print(f"Число {n} является нечетным.")


print_square()
check_even_odd()
