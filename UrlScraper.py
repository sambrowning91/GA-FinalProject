# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:50:55 2016

@author: Sam Browning

Writing a script to loop over a list of urls, filter out all the crap and return URL, Date, Author, Body and other relevant columns
"""

import time
import pandas as pd

#create string with today's date for filename
timestr = time.strftime("%Y%m%d")
#create inputfile with today's date in name
inputfile = 'StoryList-%s.csv' % timestr

df = pd.read_csv(inputfile)


#Write somefunction that will do the thing to the link, then loop over all the links and do the function
#for i in df["PageLinks"]:
    #SOMEFUNCTION()

#what do we want the function to do? 
