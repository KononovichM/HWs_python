import re

file_name = "text.txt"


def find_dates():
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()
            dates = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text)
            print("Найденные даты:", dates)
    except FileNotFoundError:
        print("Файл не найден.")


def is_valid_password(password):
    if (len(password) >= 4 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password)):
        return True
    return False


def remove_duplicates(text):
    return re.sub(r"\b(\w+)(\s+\1\b)+", r"\1", text)


if __name__ == "__main__":
    find_dates()

    test_passwords = ["Test1", "pass", "1234", "GoodPass123"]
    for pwd in test_passwords:
        print(f"Пароль '{pwd}' {'корректен' if is_valid_password(pwd) else 'некорректен'}")

    test_text = "Довольно распространённая ошибка ошибка — это лишний повтор повтор слова слова. " \
                "Смешно, не не правда ли? Не нужно портить хор хоровод."
    print("Исправленный текст:", remove_duplicates(test_text))
