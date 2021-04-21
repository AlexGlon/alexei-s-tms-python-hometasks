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
        characters = get_characters()
        json.dump(characters, file, indent=4)
    return characters


def load_file():
    with open('characters.json', 'r') as file:
        characters = json.load(file)
    return characters


def list_load():
    import os
    if not os.path.isfile('characters.json'):
        print('Loading character list from the external source...')
        return save_file()
    else:
        print('Loading character list from the local source...')
        return load_file()
# в результате вам вернется список словарей-персонажей, в которых вам необходимы следующие ключи:
# name - имя персонажа
# status - жив персонаж или нет
# species - раса персонажа
# gender - пол персонажа
# location - name - где персонаж проживает
