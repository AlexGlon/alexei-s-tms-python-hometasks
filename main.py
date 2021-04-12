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

    # print(requests.get(url).text)

    return requests.get(url).text


def input_interpreter(user_input: str) -> None:
    """Calls a specific request handler function"""
    if user_input.split()[0].lower() == "show":
        show(user_input)
    elif user_input.split()[0].lower() == "urlcontains":
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
    request = [requested, math.ceil(requested / 30)]
    print(f"You've requested {request[0]} articles -- that'd require loading {request[1]} pages.")

    page_iter = 1
    total_iter = 1
    while page_iter <= request[1]:
        received = get_page(page_iter)

        soup = BeautifulSoup(received, 'html.parser')

        headers = soup.find_all('tr', class_="athing")
        followups = soup.find_all('td', class_="subtext")

        onpage_iter = 1
        for iteration in headers:
            if total_iter > request[0]:
                break

            header_processed = str(iteration)
            followup_processed = str(followups[onpage_iter-1])
            # print(f"{header_processed}\n\n{followup_processed}")

            author = ''.join(re.findall('<a class="hnuser".*?\">(.*?)</a>', followup_processed))
            link = ''.join(re.findall('href=\"(https?://.*?)\"', header_processed))
            title = ''.join(re.findall('storylink\".*?">(.*?)</a>', header_processed))
            print(f"{total_iter}. Title: {title}\nURL: {link}\nAuthor: {author}")

            total_iter += 1
            onpage_iter += 1
        page_iter += 1


def urlcontains(user_input: str) -> None:
    """Handles requests with `urlcontains` header"""
    pass


while True:
    user_input = input("Please enter your command (or enter 'EXIT' to exit):")
    if user_input.upper() == 'EXIT':
            break
    input_interpreter(user_input)
