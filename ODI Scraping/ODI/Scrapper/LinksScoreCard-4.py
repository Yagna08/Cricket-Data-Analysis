from bs4 import BeautifulSoup

with open('ODI Scraping\ODI\Scrapper\ODILinksList.txt', 'r', encoding='utf-8', errors='ignore') as f:
      links = f.readlines()
      for i in range(len(links)):
            links[i] = links[i].strip('\n')

a=[]
for website in links:
    with open('ODI Scraping\ODI\ListHtml\\'+website.split('/')[2]+'.html','r', encoding='utf-8', errors='ignore') as file:
        soup=BeautifulSoup(file,features="html.parser")
        div = soup.findAll('div',class_='ds-p-4 ds-border-y ds-border-line')
        for i in div:
            a.append(i.find('a')['href'])

ScoreCardLink=[]

for i in a:
    if i.find('india')!=-1:
        ScoreCardLink.append(i)

with open('ODI Scraping\ODI\Scrapper\ScoreCardLinks.txt', 'w') as f:
      for i in ScoreCardLink:
            f.write(i+'\n') 
