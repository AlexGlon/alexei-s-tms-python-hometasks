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


# TODO: rework this function's logic so that it parses all the arguments
# TODO: break down this function's logic into separate funcs maybe?

def input_interpreter(user_input: str) -> None:
    """Calls a specific request handler function"""
    input_list = user_input.split()

    command = input_list[0].lower()

    # todo: turn string values into functions as soon as these functions are implemented

    command_handler = {
        'show': show,
        'urlcontains': contains_handler,
        'titlecontains': contains_handler,
        'author': contains_handler,
        'save': "save",
        'load': "load",
        'help': "help"
    }

    if command not in command_handler.keys():
        print("Invalid input. Please try again.")
        return

    # dictionary of arguments initialized with default values

    # TODO: implement handling of cases where search string has spaces

    # TODO: more arguments for load/save functions

    arg_dict = {
        'load': 30,
        'keyword': '',
        'pick': 10,
        'toprating': (lambda arg=input_list[1]: True if arg.lower() == 'toprating' else False)(),
        'points': 100,
        'contains_handler': input_list[0].split('contains')[0]
    }

    # fills `load` and `pick` arguments (and handles a case when the keyword goes after a load argument)
    iteration = 0

    try:
        for i in input_list:
            if i.isnumeric():
                arg_dict['load'] = int(i)
                if input_list[iteration + 1].isnumeric():
                    arg_dict['pick'] = int(input_list[iteration + 1])
                elif input_list[iteration + 1].isalpha():
                    arg_dict['keyword'] = input_list[iteration + 1]
                break
            iteration += 1

    except:
        pass

    try:

        # fills `keyword` argument for sure

        if input_list[1].isalnum():
            arg_dict['keyword'] = input_list[1]

        # fills `points` argument

        if input_list[1].split(':')[0] == 'points' and input_list[1].split(':')[1].isnumeric():
            arg_dict['points'] = int(input_list[1].split(':')[1])
    except:

        # TODO: handling some cases that'd cause commands not to work

        pass

    # try:
    command_handler[command](arg_dict)
    # except:
    #    print("Invalid syntax. Please try again.")


def get_title(source: str) -> str:
    """Gets article title from the corresponding HTML block"""
    string = ''.join(re.findall('storylink\".*?">(.*?)</a>', source))

    if string == '':
        return 'undefined'
    return string


def get_url(source: str) -> str:
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


def news_loader(requested):
    """Handles loading a list containing news"""

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

        onpage_iter = 0
        for iteration in headers:
            if total_iter > request['total']:
                break

            header_processed = str(iteration)
            followup_processed = str(followups[onpage_iter])
            # print(f"{header_processed}\n\n{followup_processed}")

            news_dict = {
                'author': get_author(followup_processed),
                'url': get_url(header_processed),
                'title': get_title(header_processed),
                'comments': get_comments(followup_processed),
                'rating': get_rating(followup_processed)
            }
            # print(f"{total_iter}. Title: {news_dict['title']}\n"
            #       f"URL: {news_dict['url']}\n"
            #       f"Author: {news_dict['author']}"
            #       f" || Comments: {news_dict['comments']}"
            #       f" || Rating: {news_dict['rating']}\n")

            news.append(news_dict)

            total_iter += 1
            onpage_iter += 1
        page_iter += 1

    return news


def show(arg_dict) -> None:
    """Handles requests with `show` header"""
    news = news_loader(arg_dict['load'])
    iteration = 1
    for i in news:
        print(f"{iteration}. Title: {i['title']}\n"
              f"URL: {i['url']}\nAuthor: {i['author']}"
              f" || Comments: {i['comments']}"
              f" || Rating: {i['rating']}\n")
        iteration += 1


# TODO: one function for urlcontains/titlecontains/author reqs

def contains_handler(arg_dict) -> None:
    """Handles requests with `urlcontains`, `titlecontains` and `author` headers"""

    print('Please bear in mind that this command is case-sensitive. In case no results were found, try again.')
    news = news_loader(arg_dict['load'])
    iteration = 1
    searchRE = f"({arg_dict['keyword']}.*?)"

    for i in news:
        if i[arg_dict['contains_handler']] is not None and re.findall(searchRE, i[arg_dict['contains_handler']]):
            print(f"{iteration}. Title: {i['title']}\n"
                  f"URL: {i['url']}\nAuthor: {i['author']}"
                  f" || Comments: {i['comments']}"
                  f" || Rating: {i['rating']}\n")
            iteration += 1


while True:
    user_input = input("Please enter your command (or enter 'EXIT' to exit):")
    if user_input.upper() == 'EXIT':
        break
    input_interpreter(user_input)
