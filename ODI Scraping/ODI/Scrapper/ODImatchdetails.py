from bs4 import BeautifulSoup
import pandas as pd
with open('ODI Scraping\ODI\Scrapper\ScoreCardLinks.txt','r',encoding='utf-8', errors='ignore') as f:
    links = f.readlines()

for i in range(len(links)):
    links[i] = links[i].strip('\n')
ODImainSummary = pd.DataFrame()

for link in links:
    file = open('ODI Scraping/ODI/ScoreCard/'+link.split('/')[-2]+'.html','r',encoding='utf-8', errors='ignore')
    soup=BeautifulSoup(file,features="lxml")
    matchId = []
    temp=[]
    temp_date,match_date=[],[]
    mainteam1,mainteam2=[],[]
    winner=[]
    margin=[]
    team1,team2='',''

    link_name = link.strip('\n')
    temp_name = link_name.split('/')[-2].split('-')[:-3]
    table = soup.findAll('table',class_='ds-w-full ds-table ds-table-sm ds-table-auto')
    for i in table:
        td = i.findAll('td',class_='ds-min-w-max ds-text-typo')
        for j in td:
            temp_date.append(j.text.strip())
            a = j.findAll('a',class_='ds-inline-flex ds-items-start ds-leading-none')
            for k in a:
                temp.append(k.text.strip())
            
    for i in range(len(temp)):
        if temp[i].startswith('ODI') and temp[i][8]!='0':
            matchId.append(temp[i])
    for i in range(len(temp_date)):
        if temp_date[i].endswith('(50-over match)'):
            match_date.append(temp_date[i].split('-')[0].strip())
    temp_winner=soup.findAll('p',class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')
    for i in temp_winner:
        win=i.text.strip()
        temp_win=win.split('won')
        winner.append(temp_win[0])
        temp_margin=win.split('by')
        if len(temp_margin)==2:
            margin.append(temp_margin[1])
        else:
            margin.append('No result')
    divs = soup.findAll('div',class_='ds-rounded-lg ds-mt-2')
    for div in range (len(divs)):
        span = divs[div].find('span',class_='ds-text-title-xs ds-font-bold ds-capitalize')
        if div==0:
            team1=(span.text.strip())
        else:
            team2=(span.text.strip())
    if len(team1)==0:
        team1='-'
    if len(team2)==0:
        team2='-'
    mainteam1.append(team1)
    mainteam2.append(team2)

    df = pd.DataFrame(list(zip(matchId,mainteam1,mainteam2,winner,margin,match_date)),columns=['Id','Team1','Team2','Winner','Margin','Date'])
    ODImainSummary = pd.concat([ODImainSummary,df])
print(ODImainSummary)
ODImainSummary.to_csv('ODImatchSummaryINDIA.csv')
