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


def get_title(source: str) -> str:
    """Gets article title from the corresponding HTML block"""
    string = ''.join(re.findall('storylink\".*?">(.*?)</a>', source))

    if string == '':
        return 'undefined'
    return string


def get_link(source: str) -> str:
    """Gets article link from the corresponding HTML block"""
    string = ''.join(re.findall('href=\"(https?://.*?)\"', source))

    if string == '':
        string = ''.join(re.findall('k\" href=\"(item.*?)\"', source))
        string = 'https://news.ycombinator.com/' + string

    if string == '':
        return None
    return string


def get_author(source: str) -> str:
    """Gets article author from the corresponding HTML block"""
    string = ''.join(re.findall('<a class="hnuser".*?\">(.*?)</a>', source))

    if string == '':
        return None
    return string


def get_comments(source: str) -> str:
    """Gets article comments count from the corresponding HTML block"""
    string = ''.join(re.findall(' <a href="item.*?\">(.*?)\scomments</a> </td>', source))

    if string == '':
        return '0'
    return string


def get_rating(source: str) -> str:
    """Gets article rating from the corresponding HTML block"""
    string = ''.join(re.findall('class="score".*?\">(.*?) points', source))

    if string == '':
        return '0'
    return string


# TODO: separate logic for a function that loads all the news into a list

def news_loader(user_input: str):
    requested = 0

    if user_input.split()[-1].isnumeric():
        requested = int(user_input.split()[-1])

    print(requested)
    request = {
        'total': requested,
        'pages': math.ceil(requested / 30)
    }
    print(f"You've requested {request['total']} articles -- that'd require loading {request['pages']} pages.")

    page_iter = 1
    total_iter = 1

    news = []


    while page_iter <= request['pages']:
        received = get_page(page_iter)

        soup = BeautifulSoup(received, 'html.parser')

        headers = soup.find_all('tr', class_="athing")
        followups = soup.find_all('td', class_="subtext")

        onpage_iter = 1
        for iteration in headers:
            if total_iter > request['total']:
                break

            header_processed = str(iteration)
            followup_processed = str(followups[onpage_iter - 1])
            # print(f"{header_processed}\n\n{followup_processed}")

            news_dict = {
                'author': get_author(followup_processed),
                'link': get_link(header_processed),
                'title': get_title(header_processed),
                'comments': get_comments(followup_processed),
                'rating': get_rating(followup_processed)
            }
            # print(f"{total_iter}. Title: {news_dict['title']}\n"
            #       f"URL: {news_dict['link']}\n"
            #       f"Author: {news_dict['author']}"
            #       f" || Comments: {news_dict['comments']}"
            #       f" || Rating: {news_dict['rating']}\n")

            news.append(news_dict)

            total_iter += 1
            onpage_iter += 1
        page_iter += 1

    return news


def show(user_input: str) -> None:
    """Handles requests with `show` header"""
    news = news_loader(user_input)
    iteration = 1
    for i in news:
        print(f"{iteration}. Title: {i['title']}"
              f"\nURL: {i['link']}\nAuthor: {i['author']}"
              f" || Comments: {i['comments']}"
              f" || Rating: {i['rating']}\n")
        iteration += 1

def urlcontains(user_input: str) -> None:
    """Handles requests with `urlcontains` header"""
    pass


while True:
    user_input = input("Please enter your command (or enter 'EXIT' to exit):")
    if user_input.upper() == 'EXIT':
            break
    input_interpreter(user_input)
