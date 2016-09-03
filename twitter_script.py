import urllib
from bs4 import BeautifulSoup #модуль для парсинга HTML страницы

def get_tweets(username):
    """ Получаем ссылку пользователя и текст последних его твитов """

    url = urllib.request.urlopen("https://twitter.com/" + username)
    page = BeautifulSoup(url,"lxml")
    url.close()
#js-tweet-text-container
    texts = [p.text for p in page.findAll("p")
            if ("class" in p.attrs) and
            ("js-tweet-text" in p.attrs["class"])]

    links = [a.attrs["href"] for a in page.findAll("a")
            if ("class" in a.attrs) and
            ("tweet-timestamp" in a.attrs["class"])]

    return (texts, links)

print(get_tweets("Egor4iK1613"))
