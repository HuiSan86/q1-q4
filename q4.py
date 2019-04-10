import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# Q4 (A)

url_1190s = "https://en.wikipedia.org/wiki/1990s_in_music"
html_1190s = urlopen(url_1190s)

soup = BeautifulSoup(html_1190s, 'lxml')

# Print out the raw text to a new file
text_1990s = soup.get_text()
F = open("List_90s.txt","w")
F.write(text_1990s)


# Q4 (B)
url_BS = "https://en.wikipedia.org/wiki/List_of_best-selling_music_artists#120_million_to_199_million_records"
html_BS = urlopen(url_BS)
soup = BeautifulSoup(html_BS, 'lxml')

text_BS = soup.get_text()
rows = soup.find_all('tr')


A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

# Pull out columns that are needed for further analysis
for row in rows:
    cells = row.findAll('td')
    artist = row.findAll('th',{'scope':'row'})
    if len(artist)==1:
    	A.append(artist[0].find(text=True))
    if len(cells)==6: #Only extract table body not heading
        B.append(cells[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[5].find(text=True))



df=pd.DataFrame(A[:116],columns=['Artist'])
df['Country/Market']=B[:116]
df['Period_active']=C[:116]
df['Release_year_of_first_charted_record']=D[:116]
df['Genre']=E[:116]
df['Claimed_sales']=F[:116]


with open('List_90s.txt', 'r') as file:
	data = file.read().replace('\n', '')

columns_art = df['Artist']

# Q4 (c)
# Extract the total number of best selling artist and compared with raw text from (A)
count = 0
for row_A in columns_art:
	convertToStrA = str(row_A)
	if (data.find(convertToStrA) != -1): 
		#print(row_A)
		count +=1
		
print ("Total numbers of best-selling music artists from 1990s: ")
print(count)

