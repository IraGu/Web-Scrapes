#purpose is to scrape words from website
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uopen

my_url = 'http://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_a.html'

dict_a = uopen(my_url)
dict_ha = dict_a.read()
dict_a.close()

soup_a = soup(dict_ha, "html.parser")
s_list = soup_a.find("b")

list1 = []

#find all words in body
for ele in soup_a.findChildren('b'):
    list1.append(ele.text)

#clean data, remove unnecessary words and repeats
len(list1)
list1 = list(sorted(set(list1)))
len(list1)
print(list1[1:50])

list2 = []

#remove words with special characters and less less than 5
for s in list1:
    if any(c in s for c in (" ", "'","-")) == False and len(s) > 4:
        list2.append(s)
    else:
        continue


len(list2)
print(list2[0:50])