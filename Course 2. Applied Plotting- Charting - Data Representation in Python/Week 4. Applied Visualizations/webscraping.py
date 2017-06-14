# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:37:42 2017

@author: Jie Xue
"""
import pandas as pd
import urllib
import re
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Big_Ten_Conference'
html = urllib.urlopen(url).read()

bs = BeautifulSoup(html)

table = bs.find('table', attrs={'class':'wikitable sortable'})


print(table)

rows = table.find_all('tr')

data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
data[:] = [item for item in data if item != []]

print(data)
print(data[0])
print(data[1])
print(len(data))


type(data[0][0])
re.findall(r"u'(.*?)'", data[0][0].encode('ascii','ignore'))
type(data[0][0].encode('ascii','ignore'))
print(data[0][0].encode('ascii','ignore'))




List_name = []
List_begin = []
List_join = []
for i in range(len(data)):
    List_name.append(data[i][0].encode('ascii','ignore'))
    List_begin.append(data[i][2].encode('ascii','ignore'))
    List_join.append(re.findall('\d{4}', data[i][3].encode('ascii','ignore'))[0])
print(List_name)
print(len(List_name))
print(List_begin)
print(List_join)

df = pd.DataFrame({'Name': List_name,'Begin':List_begin,'Join':List_join})
print(df)

df['Begin'] = df['Begin'].astype(int).apply(lambda x: 2017 -x)
df['Join'] = df['Join'].astype(int).apply(lambda x: 2017 -x)
print(df)

df.to_csv('big10.csv')










