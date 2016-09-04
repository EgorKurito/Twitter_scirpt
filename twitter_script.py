import urllib
from bs4 import BeautifulSoup #модуль для парсинга HTML страницы

def get_tweets(username):
    """ Gets the texts and links of username's lattest tweets """

    url = urllib.request.urlopen("https://twitter.com/" + username)
    page = BeautifulSoup(url,"lxml")
    url.close()

    texts = [p.text for p in page.findAll("p")
            if ("class" in p.attrs) and
            ("js-tweet-text" in p.attrs["class"])]

    links = [a.attrs["href"] for a in page.findAll("a")
            if ("class" in a.attrs) and
            ("tweet-timestamp" in a.attrs["class"])]

    i = 0
    while i < 19:
        print(texts[i] + ": " + " https://twitter.com/" + links[i])
        i = i + 1

get_tweets("Egor4iK1613")
