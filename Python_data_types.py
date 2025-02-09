# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
text = "www.my_site.com#about"
print(text.replace("#", "/"))

# Напишите программу, которая добавляет ‘ing’ к словам
words = ["play", "cry", "dry", "run", "walk"]
new_words = [word + "ing" for word in words]
print(new_words)

words = ["play", "cry", "dry", "run", "walk"]
msg = "ing ".join(words)+"ing"
print(msg)

# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
text = 'Ivanou Ivan'
arr = text.split()
new_text = f"{arr[1]} {arr[0]}"
print(new_text)

# Напишите программу которая удаляет пробел в начале, в конце строки
test_str = " Hello my dear friend! "
print(test_str.lstrip())
print(test_str.strip())

# Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
#Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
name = "pARiS"
corrected_name = name.capitalize()
print(corrected_name)

# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
text = "Robin Singh"
words = text.split()
print(words)


# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
text = "I love arrays they are my favorite"
words = text.split()
print(words)

# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
#Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
names = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"

text = f"Привет, {names[0]} {names[1]}! Добро пожаловать в {city} {country}"
print(text)

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
words = ["I", "love", "arrays", "they", "are", "my", "favorite"]
sentence = " ".join(words)
print(sentence)

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
# Создаем список из 10 элементов
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.insert(2, "new_value")
del my_list[6]
print(my_list)
