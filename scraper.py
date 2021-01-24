from typing import List
from bs4 import BeautifulSoup
import requests
import os
import lxml


FILE_PATH = "articles/"
LIST_NAME = "list_of_articles.txt"


def get_articles(file_path=FILE_PATH,list_article=LIST_NAME):
    articles_list = []
    with open(file_path+list_article,"r") as articles_file:
        lines = articles_file.read().splitlines()
        for line in lines:
            articles_list.append(line)
    
    return articles_list

def collect_article_text(article):
    headers = {'User-Agent': 'My User Agent 1.0', 'From':'espanto28@domain.com'}
    cookies = {'visitor_id781113-hash': '424282e29c3ee77251bb866e469b79ed3920c9ace08a5f9c0f3c2b9132c6bf51a431d3bf2448c3c6f57673a996a9a7df4f62f454'}
    html_source_code = requests.get(article,headers=headers,cookies=cookies)
    soup = BeautifulSoup(html_source_code.text,"html.parser")
    print("Writing to HTML to check output")
    with open('articles/check.html','w') as html_file:
        html_file.write(str(soup))
    print("writing file div")
    #article_div = soup.find('div',class_='entry-content')
    article_div = soup.find('div')

    return article_div 

def save_article_text(article,article_title):
    with open("articles/"+article_title+".txt","w") as write_file:
        write_file.write(article.text)


def main():
    articles_to_scrape = get_articles(FILE_PATH,LIST_NAME)
    print(articles_to_scrape)
    #article_title = articles_to_scrape[1].split("/")[2]
    for article in articles_to_scrape:
        print(article)
        article_title = article.split("/")[2]
        print(article_title)
        article_div = collect_article_text(article)
        print(article_div)
        save_article_text(article_div,article_title)
    #article_div = collect_article_text(articles_to_scrape)
    #save_article_text(article_div,article_title)

main()