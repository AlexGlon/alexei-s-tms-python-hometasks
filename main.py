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

def input_interpreter(user_input: str) -> None:
    """Calls a specific request handler function"""
    if (user_input.split()[0].lower() == "show"):
        show()
    elif (user_input.split()[0].lower() == "urlcontains"):
        urlcontains()
    else:
        print("Invalid input. Please try again.")

# TODO: separate request interpreter functions


def show():
    pass


def urlcontains():
    pass


while True:
    user_input = input("Please enter your command (or enter 'EXIT' to exit):")
    if user_input.upper() == 'EXIT':
            break
    input_interpreter(user_input)
