def get_palindromic(input_str, count):
    result = ""
    index = 0

    if count > len(input_str):
        raise ValueError("Неправильное число символов!")

    while index < count:
        result += input_str[index]

        index += 1

    reversed_str = result[::-1]
    remove_last_char = result[:count-1]

    return remove_last_char + reversed_str


s = "abcdef"
print(get_palindromic(s, 1))
print(get_palindromic(s, 2))
print(get_palindromic(s, 3))
print(get_palindromic(s, 4))
