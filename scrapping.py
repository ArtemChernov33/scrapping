import bs4
import requests
from pprint import pprint
from bs4 import BeautifulSoup

KEYWORDS = ['Solidity: комментарии', 'Geo data in Python', 'Кофеин: как это работает?', '2']

url = 'https://habr.com/ru/all'

response = requests.get(url)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all("article")

def get_data():
    for article in articles:
        titles = article.find_all(class_="tm-article-snippet__title tm-article-snippet__title_h2")
        titles = set(title.text.strip() for title in titles)
        for title in titles:
            if title in KEYWORDS:
                date = article.find(class_="tm-article-snippet__datetime-published").time['title']
                href = article.find(class_="tm-article-snippet__title-link").attrs['href']
                url_ = ("https://habr.com" + href)
                rezult = print(f'Дата выпуска статьи:{date}. Название статьи:{title}. Ссылка на статью:{url_}')
                pprint(rezult)

if __name__ == '__main__':
    get_data()