import get
import math
from bs4 import BeautifulSoup


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
        received = get.get_page(page_iter)

        soup = BeautifulSoup(received, 'html.parser')

        headers = soup.find_all('tr', class_="athing")
        followups = soup.find_all('td', class_="subtext")

        onpage_iter = 0
        for iteration in headers:
            if total_iter > request['total']:
                break

            header_processed = str(iteration)
            followup_processed = str(followups[onpage_iter])

            news_dict = {
                'author': get.get_author(followup_processed),
                'url': get.get_url(header_processed),
                'title': get.get_title(header_processed),
                'comments': get.get_comments(followup_processed),
                'rating': get.get_rating(followup_processed)
            }
            news.append(news_dict)

            total_iter += 1
            onpage_iter += 1
        page_iter += 1

    return news
