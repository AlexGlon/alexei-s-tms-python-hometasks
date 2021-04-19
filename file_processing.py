import json

# Возьмите url для api данных сериала Рик и Морти
url = 'https://rickandmortyapi.com/api/character/'

# используя модуль `requests` и функцию `get` из этого модуля получите json ответа
# и по ключу `results` получите список персонажей сериала


def get_characters():
    import requests

    return requests.get(url).json()['results']


def save_file():
    with open('characters.json', 'w') as file:
        json.dump(get_characters(), file, indent=4)
    pass


def load_file():
    with open('characters.json', 'r') as file:
        characters = json.load(file)
    return characters


def list_load():
    pass
# в результате вам вернется список словарей-персонажей, в которых вам необходимы следующие ключи:
# name - имя персонажа
# status - жив персонаж или нет
# species - раса персонажа
# gender - пол персонажа
# location - name - где персонаж проживает
