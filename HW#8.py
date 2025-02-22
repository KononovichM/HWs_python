# программа загадывает число
# create array with numbers from 0 to 9
import random
num_massiv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(num_massiv)

first_four = num_massiv[:4]
# uncomment this line for debug mode
# print(first_four)


def input_compare(numbers):
    # программа просит ввести число в консоль
    print("Введите четырехзначное число:")

    # программа считывает что ввели в консоль
    input_number = input()
    letters = list(input_number)
    print(letters)

    # программа сравнивает то что ввели с тем что загадали
    # for переменная in  лист/массив
    Cows = 0
    Bulls = 0
    for index, letter in enumerate(letters):
        print(index, letter)
    # print(letter in first_four)
        if letter in numbers and index == numbers.index(letter):
            print("bull")
            Bulls = Bulls + 1

        else:
            if letter in numbers:
                print("Cow")
                Cows = Cows + 1

    print("Cow:", Cows)
    print("Bull", Bulls)
    return Bulls


# программа выдает ответ

while True:
    bulls_count = input_compare(first_four)
    if bulls_count == 4:
        break


# Пирамида
def print_pyramid(lines):
    for line_number in range(lines):
        spaces = " " * (lines - line_number - 1)
        stars = "*" * (2 * line_number + 1)
        print(spaces + stars)


print_pyramid(10)


# Statues
def missing_statues(statues):
    return (max(statues)) - (min(statues)) + 1 - len(statues)


statues_2 = [6, 2, 3, 8]
print(missing_statues(statues_2))
