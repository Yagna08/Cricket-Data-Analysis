from bs4 import BeautifulSoup
import pandas as pd
# import asyncio
# from pyppeteer import launch

# async def main(website):
#         browser = await launch()
#         page = await browser.newPage()
#         await page.goto(website)
#         await asyncio.sleep(3)
#         html = await page.content()
#         await browser.close()
#         return html


players_list = [
    'https://www.espncricinfo.com/cricketers/arshdeep-singh-1125976',
    'https://www.espncricinfo.com/cricketers/avesh-khan-694211',
    'https://www.espncricinfo.com/cricketers/axar-patel-554691',
    'https://www.espncricinfo.com/cricketers/bhuvneshwar-kumar-326016',
    'https://www.espncricinfo.com/cricketers/chetan-sakariya-1131754',
    'https://www.espncricinfo.com/cricketers/deepak-chahar-447261',
    'https://www.espncricinfo.com/cricketers/deepak-hooda-497121',
    'https://www.espncricinfo.com/cricketers/hardik-pandya-625371',
    'https://www.espncricinfo.com/cricketers/ishan-kishan-720471',
    'https://www.espncricinfo.com/cricketers/jasprit-bumrah-625383',
    'https://www.espncricinfo.com/cricketers/jayant-yadav-447587',
    'https://www.espncricinfo.com/cricketers/kl-rahul-422108',
    'https://www.espncricinfo.com/cricketers/kedar-jadhav-290716',
    'https://www.espncricinfo.com/cricketers/krishnappa-gowtham-424377',
    'https://www.espncricinfo.com/cricketers/krunal-pandya-471342',
    'https://www.espncricinfo.com/cricketers/kuldeep-yadav-559235',
    'https://www.espncricinfo.com/cricketers/manish-pandey-290630',
    'https://www.espncricinfo.com/cricketers/mayank-agarwal-398438',
    'https://www.espncricinfo.com/cricketers/mohammed-shami-481896',
    'https://www.espncricinfo.com/cricketers/mohammed-siraj-940973',
    'https://www.espncricinfo.com/cricketers/navdeep-saini-700167',
    'https://www.espncricinfo.com/cricketers/nitish-rana-604527',
    'https://www.espncricinfo.com/cricketers/prasidh-krishna-917159',
    'https://www.espncricinfo.com/cricketers/prithvi-shaw-1070168',
    'https://www.espncricinfo.com/cricketers/rahul-chahar-1064812',
    'https://www.espncricinfo.com/cricketers/ravi-bishnoi-1175441',
    'https://www.espncricinfo.com/cricketers/ravichandran-ashwin-26421',
    'https://www.espncricinfo.com/cricketers/ravindra-jadeja-234675',
    'https://www.espncricinfo.com/cricketers/rishabh-pant-931581'
    'https://www.espncricinfo.com/cricketers/ruturaj-gaikwad-1060380',
    'https://www.espncricinfo.com/cricketers/sanju-samson-425943',
    'https://www.espncricinfo.com/cricketers/shahbaz-ahmed-1159711',
    'https://www.espncricinfo.com/cricketers/shardul-thakur-475281',
    'https://www.espncricinfo.com/cricketers/shikhar-dhawan-28235',
    'https://www.espncricinfo.com/cricketers/shivam-dube-714451',
    'https://www.espncricinfo.com/cricketers/shreyas-iyer-642519',
    'https://www.espncricinfo.com/cricketers/shubman-gill-1070173',
    'https://www.espncricinfo.com/cricketers/suryakumar-yadav-446507',
    'https://www.espncricinfo.com/cricketers/umran-malik-1246528',
    'https://www.espncricinfo.com/cricketers/venkatesh-iyer-851403',
    'https://www.espncricinfo.com/cricketers/vijay-shankar-477021',
    'https://www.espncricinfo.com/cricketers/virat-kohli-253802',
    'https://www.espncricinfo.com/cricketers/washington-sundar-719715',
    'https://www.espncricinfo.com/cricketers/yuzvendra-chahal-430246',
    'https://www.espncricinfo.com/cricketers/mukesh-kumar-926851'
]

# for i in players_list:
#     result = asyncio.get_event_loop().run_until_complete(main(i))
#     open(i.split('/')[-1] + '.html','w', encoding='utf-8').write(result)

# print(len(players_list))
name,battingStyle,bowlingStyle,role,image,fieldingPosition = [],[],[],[],[],[]

for link in players_list:
    fileName = 'Players/'+link.split('/')[-1]+'.html'
    file = open(fileName,'r',encoding='utf-8', errors='ignore')
    soup=BeautifulSoup(file,features="lxml")

    divs = soup.find('div',class_='ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-4 ds-mb-8')
    imgDiv = soup.find('div',class_='ds-p-0')
    imgdivdiv = imgDiv.find('div',class_='ds-ml-auto ds-w-48 ds-h-48')
    img = imgDiv.find('img')

    print(imgdivdiv)
    fetchBattingStyle = divs.findAll('span',class_='ds-text-title-s ds-font-bold ds-text-typo')
    temp=[]
    for i in fetchBattingStyle:
        temp.append(i.text.strip())

    name.append(temp[0])
    battingStyle.append(temp[-3])
    role.append(temp[-1])
    if temp[-2] == 'Wicketkeeper':
        fieldingPosition.append(temp[-2])
        bowlingStyle.append('None')
    else:
        bowlingStyle.append(temp[-2])
        fieldingPosition.append('None')


df = pd.DataFrame(list(zip(name,battingStyle,bowlingStyle,fieldingPosition,role)),columns=['Name','Batting Style','Bowling Style','Fielding Position','Playing Role'])
print(df)
df.to_csv('dim_players.csv')
