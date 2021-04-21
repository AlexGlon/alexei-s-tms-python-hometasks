import json


def get_characters():
    import requests
    url = 'https://rickandmortyapi.com/api/character/'

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
