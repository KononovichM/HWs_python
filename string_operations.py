test_string = "Моя собака любит мягкие игрушки"

first_char = test_string[0]
print("1й символ:", first_char)

last_char = test_string[-1]
print("Последний символ:", last_char)

third_char_from_start = test_string[2]
print("3 символ с начала:", third_char_from_start)

third_char_from_end = test_string[-3]
print("3 символ с конца:", third_char_from_end)

string_length = len(test_string)
print("Длина:", string_length)

reversed = test_string[::-1]
print("Перевернутая строка:", reversed)

first_eight_chars = test_string[:8]
print("Первые 8 символов:", first_eight_chars)
