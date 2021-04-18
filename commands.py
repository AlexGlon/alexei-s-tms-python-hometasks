import news_loader as news_l

import json
import re


def output(news, arg_dict) -> None:
    iteration = 1
    for i in news:
        if arg_dict['points_arg'] and i['rating'] < arg_dict['points']:
            continue

        print(f"{iteration}. Title: {i['title']}\n"
              f"URL: {i['url']}\nAuthor: {i['author']}"
              f" || Comments: {i['comments']}"
              f" || Rating: {i['rating']}\n")
        iteration += 1

        if ((arg_dict['toprating'] or arg_dict['points_arg']) and iteration > arg_dict['pick']) \
                or (iteration > arg_dict['load']):
            break


def show(arg_dict) -> None:
    """Handles requests with `show` header"""
    news = news_l.news_loader(arg_dict['load'])
    if arg_dict['toprating']:
        news = sorted(news, key=lambda i: -i['rating'])

    output(news, arg_dict)


def save(arg_dict) -> None:
    """Handles requests with `save` header"""

    news = news_l.news_loader(arg_dict['load'])

    with open('result.json', 'w') as file:
        json.dump(news, file, indent=4)


def load(arg_dict) -> None:
    """Handles requests with `load` header"""

    with open('result.json', 'r') as file:
        news = json.load(file)

    output(news, arg_dict)


def contains_handler(arg_dict) -> None:
    """Handles requests with `urlcontains`, `titlecontains` and `author` headers"""

    print('Please bear in mind that this command is case-sensitive. In case no results were found, try again.')
    news = news_l.news_loader(arg_dict['load'])
    iteration = 1
    searchRE = f"({arg_dict['keyword']}.*?)"

    for i in news:
        if i[arg_dict['contains_handler']] is not None and re.findall(searchRE, i[arg_dict['contains_handler']]):
            print(f"{iteration}. Title: {i['title']}\n"
                  f"URL: {i['url']}\nAuthor: {i['author']}"
                  f" || Comments: {i['comments']}"
                  f" || Rating: {i['rating']}\n")
            iteration += 1


def help(arg_dict) -> None:
    """Handles `help` request"""
    print(f"\nshow [10] - displays first [10] articles (30 by default).\n"
          f"show toprating [50] [10] - displays first [10] articles with the highest rating among first [50] articles total.\n"
          f"show points:[100] [50] [10] - displays first [10] articles with rating above [100] among first [50] articles total.\n\n"
          f"urlcontains [50] keyword - displays all articles that have a specified case-sensitive keyword in their URLs among the first [50] articles (30 by default).\n\n"
          f"titlecontains [50] keyword - displays all articles that have a specified case-sensitive keyword in their titles among the first [50] articles (30 by default).\n\n"
          f"author [50] keyword - displays all articles that have a specified case-sensitive keyword in their authors' nicknames among the first [50] articles (30 by default).\n\n"   
          f"save [300] - saves [300] articles into a JSON file.\n\n"
          f"load [15] - loads and displays [15] articles from a JSON file.\n\n"
          f"help all - displays 'help' command.\n\n")
