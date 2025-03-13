import json


def find_best_club(json_file1):
    with open(json_file1, "r", encoding="utf-8") as file:
        clubs = json.load(file)

    best_club = max(clubs, key=lambda club: club["wins"])

    print('Клуб с наибольшим количеством побед:')
    print(f'Название: {best_club["name"]}')
    print(f'Страна: {best_club["country"]}')
    print(f'Количество побед: {best_club["wins"]}')


json_file = "clubs.json"
find_best_club(json_file)
