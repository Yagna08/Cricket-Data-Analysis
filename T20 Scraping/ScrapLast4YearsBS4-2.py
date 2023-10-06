from bs4 import BeautifulSoup

file=open('T20 Scraping\T20s.html','r', encoding='utf-8')

soup=BeautifulSoup(file,features="html.parser")
div = soup.find('div',class_='ds-overflow-x-auto ds-scrollbar-hide')
td = div.findAll('td', class_ = 'ds-min-w-max')

l = []

for t in td:
    links = t.findAll('a',class_='ds-inline-flex ds-items-start ds-leading-none')
    for link in links:
            l.append(link['href'])

links = l[39:]

with open('T20 Scraping\T20LinksList.txt', 'w') as f:
      for i in links:
            f.write(i+'\n')