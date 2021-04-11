import requests

BASE_URL = 'https://news.ycombinator.com/'


def get_page(page: int = 1) -> str:
    """Returns html of specified hacker news feed `page`"""
    assert page >= 1

    url = BASE_URL
    if page > 1:
        url = f'{BASE_URL}?p={page}'

    return requests.get(url).text

# TODO: user input interpreter function

# TODO: separate request interpreter functions


while True:
    user_input = input("Please enter your command (or enter 'EXIT' to exit):")
    if user_input == 'EXIT':
            break
