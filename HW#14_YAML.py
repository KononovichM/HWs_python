import yaml

yaml_file = "books.yaml"


def read_books():
    with open(yaml_file, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
        return data if data else {"books": []}


def add_book():
    books_data = read_books()

    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год выпуска: ")

    books_data["books"].append({"title": title, "author": author, "year": int(year)})

    with open(yaml_file, "w", encoding="utf-8") as file:
        yaml.dump(books_data, file, allow_unicode=True, default_flow_style=False)

    print(f'Книга "{title}" успешно добавлена!')


while True:
    print("\n1. Показать книги")
    print("2. Добавить книгу")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        books = read_books()["books"]
        if books:
            print("\nСписок книг:")
            for book in books:
                print(f'{book["title"]} - {book["author"]} ({book["year"]})')
        else:
            print("Список книг пуст.")

    elif choice == "2":
        add_book()

    elif choice == "3":
        print("Выход из программы.")
        break

    else:
        print("Неверный ввод, попробуйте снова.")
