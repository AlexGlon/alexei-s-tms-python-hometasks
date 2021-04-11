import requests
import math

BASE_URL = 'https://news.ycombinator.com/'


def get_page(page: int = 1) -> str:
    """Returns html of specified hacker news feed `page`"""
    assert page >= 1

    url = BASE_URL
    if page > 1:
        url = f'{BASE_URL}?p={page}'

    return requests.get(url).text

def input_interpreter(user_input: str) -> None:
    """Calls a specific request handler function"""
    if (user_input.split()[0].lower() == "show"):
        show(user_input)
    elif (user_input.split()[0].lower() == "urlcontains"):
        urlcontains(user_input)
    else:
        print("Invalid input. Please try again.")

# TODO: separate request interpreter functions


def show(user_input: str) -> None:
    """Handles requests with `show` header"""
    requested = 0

    if user_input.split()[-1].isnumeric():
        requested = int(user_input.split()[-1])

    print(requested)
    request = []
    request.append(requested)
    request.append(math.ceil(requested / 30))
    print(f"You've requested {request[0]} articles -- that'd require to load {request[1]} pages.")
    pass


def urlcontains(user_input: str) -> None:
    """Handles requests with `urlcontains` header"""
    pass


while True:
    user_input = input("Please enter your command (or enter 'EXIT' to exit):")
    if user_input.upper() == 'EXIT':
            break
    input_interpreter(user_input)
