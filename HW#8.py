# программа загадывает число
# create array with numbers from 0 to 9
import random
num_massiv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random.shuffle(num_massiv)
print(num_massiv)
first_four = num_massiv[:4]
print(first_four)
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
    #print(letter in first_four)
    if letter in first_four and index == first_four.index(letter):
        print("bull")
        Bulls = Bulls +1

    else:
        if letter in first_four:
            print("Cow")
            Cows = Cows + 1

print("Cow:", Cows)
print("Bull", Bulls)
# программа выдает ответ


# Пирамида
def print_pyramid(lines):
    for line_number in range(lines):
        spaces = " " * (lines - line_number - 1)
        stars = "*" * (2 * line_number + 1)
        print(spaces + stars)

def sum(a,b):
    print(a+b)

print_pyramid(10)


#Statues
def missing_statues(statues):
    return(max(statues))-(min(statues)) + 1 - len(statues)
statues = [6, 2, 3, 8]
print(missing_statues(statues))

# def missing_statues_2(statues):
# сортируем
statues = [6, 2, 3, 8]
statues = statues.sort()
print(statues)