#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 14:33:48 2021

@author: martimarti
"""

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import xlsxwriter
import os
from IPython.display import HTML
import glob
import csv
import pandas
import time
# from trafilatura import sitemaps
import json
import numpy as np
webpage='https://www.biometricupdate.com/sitemap-index-1.xml'
page = requests.get('https://www.biometricupdate.com/sitemap-index-1.xml')
 
soup = BeautifulSoup(page.content, features="xml")

links=soup.find_all(['loc', 'lastmod',])
df=pd.DataFrame(links)

links_new=soup.find_all('loc')

links_mod=soup.find_all('lastmod')

initial_map=[]
links_new_list=[]
links_mod_list=[]
for link in links:
    initial_map.append(link.text)
    
for link_new in links_new:
    links_new_list.append(link_new.text) 
    
for link_mod in links_mod:    
    links_mod_list.append(link_mod.text)   

data = { 'links': links_new_list, 'mod':links_mod_list}
 
df = pd.DataFrame(data, columns = ['links','mod'])


####################
all_links=[]

# links_new=soup.find_all('loc')
for link_new_1 in links_new_list:


    page1=requests.get(link_new_1)

    soup1=BeautifulSoup(page1.content, features="xml")

    
    links_new=soup1.find_all('loc')
 
    
    for x in links_new:
    
        all_links.append(x.text)   
        
################

###### Open each link and grab the json #######
dict1=[]
dict1_links=[]

for x in range(0,len(all_links)):
    
    try:
        for all in all_links:
            page2 = requests.get[19500:]
            # soup2=BeautifulSoup(page2.content, features='html.parser')
            # all_new=soup2.select('type')
            soup3=BeautifulSoup(page2.text, features='html.parser')
            data2=json.loads("".join(soup3.find("script", {"type":"application/ld+json"}).contents), strict=False)
            dict1.append(data2)
            dict1_links.append(all)
    except Exception:
        pass
 

#############    list of dicts to DataFrame

df_dicts = pd.DataFrame(dict1) 
df_dicts_links=pd.DataFrame(dict1_links)     
        
######################## save to csv or excel

# df_dicts.to_excel(r'/Users/martimarti/Desktop/python/scraping/scraped_060621.xlsx', 'ALL')    


# ############### NOW   Identifies the country THIS CREATE THE DATAFRAME FOR THE COUNTRY###################################################

# countries=["uk|UK", 'France|france', 'Germany|germany']

# country=df_dicts.apply(lambda row: row.astype(str).str.contains('UK').any(), axis=1)

# mask = np.column_stack([df_dicts[col].str.contains(r"government", na=False) for col in df_dicts])
# country_df=df_dicts.loc[mask.any(axis=1)]
# country_df.to_excel(r'/Users/martimarti/Desktop/python/scraping/scraped_060621_France.xlsx', 'France')    


# ############## create a new column 
# word=['government', 'biometrics', 'weapons']

# word_df = pd.DataFrame(word)
# word_df.columns=['word']


# pat = r'({})'.format(word_df['word'].str.cat(sep='|'))

# country_df['targeted_words'] = country_df['articleBody'].str.extract(pat, expand=False)


#######################






    
    