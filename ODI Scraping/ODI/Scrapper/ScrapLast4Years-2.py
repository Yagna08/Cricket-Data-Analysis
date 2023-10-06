from bs4 import BeautifulSoup

file=open('ODI Scraping\ODI\Scrapper\Odis.html','r', encoding='utf-8')

soup=BeautifulSoup(file,features="html.parser")
div = soup.find('div',class_='ds-overflow-x-auto ds-scrollbar-hide')
td = div.findAll('td', class_ = 'ds-min-w-max')

l = []

for t in td:
    links = t.findAll('a',class_='ds-inline-flex ds-items-start ds-leading-none')
    for link in links:
            l.append(link['href'])

links = l[-20:]

with open('ODI Scraping\ODI\Scrapper\ODILinksList.txt', 'w') as f:
      for i in links:
            f.write(i+'\n')