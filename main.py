import requests
import math
import re
from bs4 import BeautifulSoup

BASE_URL = 'https://news.ycombinator.com/'


def get_page(page: int = 1) -> str:
    """Returns html of specified hacker news feed `page`"""
    assert page >= 1

    url = BASE_URL
    if page > 1:
        url = f'{BASE_URL}?p={page}'

    print(f"Loading page {page}...")

    print(requests.get(url).text)

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
    print(f"You've requested {request[0]} articles -- that'd require loading {request[1]} pages.")

    # TODO: limit regex generator func

    LIMIT_RE = f"class = \"rank\">{requested}."
    # print(LIMIT_RE)

    i = 1
    while i <= request[1]:
        received = get_page(i)

        soup = BeautifulSoup(received, 'html.parser')
        print(soup.title)

        links = []
        authors = []

        #links = re.findall('title\"><a href=\"(https://.*?)\"' or 'title\"><a href=\"(.*?)\"', received)
        #authors = re.findall('hnuser\">(.*?)<', received)
        #links = soup.find_all('a', class_="storylink")
        #authors = soup.find_all('a', class_="hnuser")
        headers = soup.find_all('tr', class_="athing")
        followups = soup.find_all('td', class_="subtext")

        k=1
        for iteration in headers:
            print(f"{k} {iteration}")
            k += 1

        k = 1
        for iteration in headers:
            processed = str(iteration)
            print(processed)
            author = iteration.find_all(string=re.compile('title\"><a href=\"(https://.*?)\"'))
            link = ''.join(re.findall('href=\"(https://.*?)\"' or 'href=\"(.*?)\"', processed))
            title = ''.join(re.findall('storylink\".*?">(.*?)</a>', processed))
            #author = re.findall('hnuser\">(.*?)<', str(iteration))
            #link = re.findall('title\"><a href=\"(https://.*?)\"' or 'title\"><a href=\"(.*?)\"', str(iteration))
            print(f"{k}. {title} || {link}")
            k += 1
        i += 1
    pass


def urlcontains(user_input: str) -> None:
    """Handles requests with `urlcontains` header"""
    pass


while True:
    user_input = input("Please enter your command (or enter 'EXIT' to exit):")
    if user_input.upper() == 'EXIT':
            break
    input_interpreter(user_input)
