# Напишите программу, которая бы работала следующим образом - находила символ "#"
# и если этот символ найден - удаляла предыдущий символ из строки.
def solution_1(text):
    result = []

    for char in text:
        if char == "#":
            if result:
                result.pop()
        else:
            result.append(char)

    return "".join(result)


# Проверка с выводом результатов
test_cases = [
    ("a#bc#d", "bd"),
    ("abc#d##c", "ac"),
    ("abc##d######", ""),
    ("#######", ""),
    ("", ""),
]

for input_text, expected_output in test_cases:
    assert solution_1(input_text) == expected_output


# Cвечи
def solution(candle_number, make_new):
    total_burned = candle_number
    leftovers = candle_number

    while leftovers >= make_new:
        new_candles = leftovers // make_new
        total_burned = total_burned + new_candles
        leftovers = new_candles + (leftovers % make_new)

    return total_burned


# Проверка работоспособности
assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2


# Подсчет количества букв
def compress_string(text):
    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(text[i - 1] + (str(count) if count > 1 else ""))
            count = 1

    result.append(text[-1] + (str(count) if count > 1 else ""))

    return "".join(result)


# Проверка работоспособности
assert compress_string("cccbba") == "c3b2a"
assert compress_string("abeehhhhhccced") == "abe2h5c3ed"
assert compress_string("aaabbceedd") == "a3b2ce2d2"
assert compress_string("abcde") == "abcde"
assert compress_string("aaabbdefffff") == "a3b2def5"
