# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 16:22:42 2016

@author: Sam Browning
"""

from bs4 import BeautifulSoup
import urllib
import csv
import time

#retrieve html content of all stories page on citywire and write to txt file
urllib.urlretrieve("http://citywire.co.uk/wealth-manager/news/all-stories/list", "Allstories.txt")
#open file
htmldoc = open("Allstories.txt")
#create soup
soup = BeautifulSoup(htmldoc, "lxml")
#create empty list to hold page links
page_links = []
#loop through html file and find all relevant links
### The second part of this isn't working - need to fix later (want to ignore most popular list items as they contain dupes)
for link in soup.find_all("a", class_="media__entry-link"):
    if "most-popular-list" in link:
        pass
    else:
        page_links.append(link.get('href'))

#create string with today's date for filename
timestr = time.strftime("%Y%m%d")
#create outputfile with today's date in name
outputfile = 'StoryList-%s.csv' % timestr
#open file and write links to file
with open(outputfile,"w") as thefile:
    wr = csv.writer(thefile, quoting=csv.QUOTE_ALL)
    wr.writerow(page_links)


