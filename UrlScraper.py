# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:50:55 2016

@author: Sam Browning

Writing a script to loop over a list of urls, filter out all the crap and return URL, Date, Author, Body and other relevant columns
"""

import time
import pandas as pd
from bs4 import BeautifulSoup
import requests

#create string with today's date for filename
timestr = time.strftime("%Y%m%d")
#create inputfile with today's date in name
inputfile = 'StoryList-%s.csv' % timestr

df = pd.read_csv(inputfile)

#Need to hack at this to make sure they all have citywire.co.uk/wealth-manager appended
for i in df["PageLinks"]:
    df["FullLink"] = 'http://citywire.co.uk' + df["PageLinks"]

#what do we want the function to do? Want it to go to the link, grab the text, process the text (i.e. lower case it and remove 
#stopwords etc.) Then stick the text in the DataFrame

def ScrapeArticleHead(link):
    #retrieve html content of story page on citywire and write to txt file
    page = requests.get(link)
    #open file
    htmldoc = page.text
    #create soup
    soup = BeautifulSoup(htmldoc, "html.parser")
    #get header
    return soup.h1.get_text(strip=True)
    
def ScrapeArticleBod(link):
    #retrieve html content of story page on citywire and write to txt file
    page = requests.get(link)
    #open file
    htmldoc = page.text
    #create soup
    soup = BeautifulSoup(htmldoc, "html.parser")
    #get the important bits of the html doc
    #get body
    return soup.find_all("div", class_='article-body')

def ScrapeArticleDateTime(link):
    #retrieve html content of story page on citywire and write to txt file
    page = requests.get(link)
    #open file
    htmldoc = page.text
    #create soup
    soup = BeautifulSoup(htmldoc, "html.parser")
    #get the important bits of the html doc
    #get body
    return soup.time

def ScrapeArticleAuthor(link):
    #retrieve html content of story page on citywire and write to txt file
    page = requests.get(link)
    #open file
    htmldoc = page.text
    #create soup
    soup = BeautifulSoup(htmldoc, "html.parser")
    #get the important bits of the html doc
    #get body
    return soup.find_all("a", class_="article-meta__author")

df["Time"] = df["FullLink"].apply(ScrapeArticleDateTime)
df["Author"] = df["FullLink"].apply(ScrapeArticleAuthor)
df["Header"] = df["FullLink"].apply(ScrapeArticleHead)
df["Body"] = df["FullLink"].apply(ScrapeArticleBod)

#clean up time and author a bit
df["Time"] = df.Time.apply(lambda x: str(x).split('"')[1])
#df["Author"] = df.Author.apply(lambda x: str(x).split('>')[1])

#df['cleanedbody']=df.Body.apply(removetags)

#save to sql database
#clean body
#process text