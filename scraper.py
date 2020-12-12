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


articles_to_scrape = get_articles(FILE_PATH,LIST_NAME)

print(articles_to_scrape[1])

##TODO Wrap this into a function
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

html_source_code = requests.get(articles_to_scrape[1],headers=headers)

soup = BeautifulSoup(html_source_code.text,"html.parser") ##TODO figure out how to deal with 403 errors

#print(soup.prettify())

article_div= soup.find('div',class_='entry-content')
#print(article_div.text)
##TODO Wrap this into a function
article_title = articles_to_scrape[1].split("/")[2]

with open("articles/"+article_title+".txt","w") as write_file:
    write_file.write(article_div.text)