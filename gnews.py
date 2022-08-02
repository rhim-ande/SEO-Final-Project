import requests
import os
from random import sample

apikey = os.environ.get('gn_apikey')


def get_articles(apikey):
    url = "https://gnews.io/api/v4/search?q={}&lang={}&token={}" .format(
        "black sign language", "en", apikey)
    news = requests.get(url)
    news_data = news.json()
    each_article = news_data['articles']
    articles_list = []
    for article in each_article:
        if article['source']['name'] != 'The Nation':
            articles_list.append([article['title'], article['description'],
                                 article['url'], article['source']['name']])

    results = sample(articles_list, 3)

    return results
