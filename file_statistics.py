def get_file_info(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.readlines()

    num_lines = len(content)
    num_words = sum(len(line.split()) for line in content)
    num_chars = sum(len(line) for line in content)

    stats = [
        f"Количество строк: {num_lines}",
        f"Количество слов: {num_words}",
        f"Количество букв: {num_chars}"
    ]

    with open(file_name, "a", encoding="utf-8") as file:
        file.write("\n" + "\n".join(stats) + "\n")

    print("\n".join(stats))


file_statistics = "file_statistics.txt"
get_file_info(file_statistics)
