import streamlit as st
from database import getArticleByCategory
import sys
import logging
import datetime
from pysitemap import crawler
from database import getUrlByKeyword
import asyncio
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def anyWebsiteScrap(kw,url):
    if __name__ == '__main__':
        if '--iocp' in sys.argv:
            from asyncio import events, windows_events
            sys.argv.remove('--iocp')
            logging.info('using iocp')
            el = windows_events.ProactorEventLoop()
            events.set_event_loop(el)
        crawler(url, kw, out_file=url.split('.')[1]+'.xml', exclude_urls=[".pdf", ".png", ".jpg", ".zip", "&", ".css", ".json"])
    list = getUrlByKeyword(kw,url)
    return list


def writeCol1(listArticle):
    with articlesHolder.beta_container():
        if include != "":
            for article in listArticle:
                if include not in article[1]:
                    listArticle.remove(article)
        if exclude != "":
            for article in listArticle:
                if exclude in article[1]:
                    listArticle.remove(article)
        if dated != "":
            for article in listArticle:
                if datetime.datetime.strptime(article[2].split()[1], '%d/%m/%Y').date() < dated:
                    listArticle.remove(article)
        if datef != "":
            for article in listArticle:
                if datetime.datetime.strptime(article[2].split()[1], '%d/%m/%Y').date() > datef:
                    listArticle.remove(article)
        for article in listArticle:
            col1.write(f'''
                * URL: {article[1]}
                * Date: {article[2]}
                * Titre: {article[3]}
                ''')


def writeCol2(listArticle):
    with UrlsHolder.beta_container():
        if include != "":
            for article in listArticle:
                if include not in article[1]:
                    listArticle.remove(article)
        if exclude != "":
            for article in listArticle:
                if exclude in article[1]:
                    listArticle.remove(article)
        for article in listArticle:
            col2.write(f'''
            * {article[1]}
            ''')


articles = []
articles2 = []
col1, col2 = st.beta_columns(2)
with col1:
    st.title('NewsLetter')
    category = st.text_input("Catégorie")
    getArt = st.button("Get articles")
    articlesHolder = st.empty()
    if getArt:
        articles = getArticleByCategory(category)
        writeCol1(articles)
with col2:
    st.title('Any Website')
    keyword = st.text_input("Keyword")
    url = st.text_input("Url")
    getUrl = st.button("Extract urls")
    UrlsHolder = st.empty()
    if getUrl:
        articles2 = getUrlByKeyword(keyword, url)
        if len(articles2) == 0 :
            articles2 = anyWebsiteScrap(keyword, url)
        writeCol2(articles2)
include = st.sidebar.text_input('Url include')
exclude = st.sidebar.text_input('Url exclude')
dated = st.sidebar.date_input('Start date')
datef = st.sidebar.date_input('End date')
st.sidebar.button('Load data')
st.sidebar.button('Clear data')
