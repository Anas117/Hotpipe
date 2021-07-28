from bs4 import BeautifulSoup
from database import insertArticle
import datetime
import requests
import sys
import logging
from pysitemap import crawler

def anyWebsiteScrap(kw,url):
    global keyword
    keyword = kw
    if __name__ == '__main__':
        if '--iocp' in sys.argv:
            from asyncio import events, windows_events
            sys.argv.remove('--iocp')
            logging.info('using iocp')
            el = windows_events.ProactorEventLoop()
            events.set_event_loop(el)
        crawler(url, kw, out_file=url.split('.')[1]+'.xml', exclude_urls=[".pdf", ".png", ".jpg", ".zip", "&"])
    '''with open(url.split('.')[1]+'.xml', 'r',encoding='cp850') as f:
        data = f.read()
    y = BeautifulSoup(data, 'lxml')
    for loc in y.find_all('loc'):
        html = requests.get(loc.text).content
        s = BeautifulSoup(html, 'lxml')
        if bool(s.find(text=re.compile(keyword))):
            print("insert")
            insertKeyword_url(keyword, loc.text)
html = requests.get(url).content
    s = BeautifulSoup(html, 'lxml')
    if bool(s.find(text=re.compile(keyword))):
        insertKeyword_url(keyword, url)
    checked.append(url)
    for link in s.find_all('a'):
        link = link.get('href')
        if globalUrl in link and link not in checked and url != link and ".png" not in link and ".pdf" not in link and ".jpg" not in link and ".zip" not in link and "&" not in link:
            print(link)
            anyWebsiteScrap(keyword,link)'''


def corpusScrape():
    limitDate = datetime.datetime.today() - datetime.timedelta(days=7)
    html = requests.get('https://www.rtflash.fr/').content
    s = BeautifulSoup(html, 'lxml')
    for categories in s.find(id="nav").find_all('ul'):
        for category in categories.find_all('a'):
            url = category.get('href')
            title = category.get('title')
            i = 1
            while i > 0:
                page = BeautifulSoup(requests.get(url).content, 'lxml')
                articles = page.find_all("ul", {"class": "article-list"})
                for article in articles:
                    date = article.find('em').text
                    if datetime.datetime.strptime(date.split()[1], '%d/%m/%Y') > limitDate:
                        img = article.find('img').get('src')
                        link = article.find('a').get('href')
                        subject = article.find('a').get('title')
                        intro = article.find('p').text
                        insertArticle(title, link, date, subject, img, intro)
                    else:
                        i = -1
                        break
                url = url + '/' + str(i)
                i = i + 1
    html = requests.get('https://b-com.com/actualite').content
    html = requests.get('https://outilscollaboratifs.com/').content
    html = requests.get('https://www.01net.com/').content
    html = requests.get('https://www.ionos.fr/digitalguide/hebergement/blogs/').content
    html = requests.get('https://www.maddyness.com/').content
    html = requests.get('https://siecledigital.fr/').content
    html = requests.get('https://www.usinenouvelle.com/').content
    html = requests.get('https://itsocial.fr/').content
    html = requests.get('https://medium.com/').content
    html = requests.get('https://www.assemblee-nationale.fr/').content
    html = requests.get('https://www.journaldunet.com/').content

corpusScrape()