import re
import requests

BASE_URL = 'https://news.ycombinator.com/'


def get_page(page: int = 1) -> str:
    """Returns html of specified hacker news feed `page`"""
    assert page >= 1

    url = BASE_URL
    if page > 1:
        url = f'{BASE_URL}?p={page}'

    print(f"Loading page {page}...")

    return requests.get(url).text


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


def get_comments(source: str) -> int:
    """Gets article comments count from the corresponding HTML block"""
    string = ''.join(re.findall(' <a href="item.*?\">(.*?)\scomments</a> </td>', source))

    if string == '':
        return 0
    return int(string)


def get_rating(source: str) -> int:
    """Gets article rating from the corresponding HTML block"""
    string = ''.join(re.findall('class="score".*?\">(.*?) points', source))

    if string == '':
        return 0
    return int(string)
