def is_palindrome(test_str):
    index = 0
    str_len = len(test_str)

    while index < (str_len / 2):
        if test_str[index] != test_str[str_len - index - 1]:
            return False
        index += 1
    return True


print(is_palindrome('шалаш'))
print(is_palindrome('киик'))
print(is_palindrome('биба'))
print(is_palindrome('стена'))
