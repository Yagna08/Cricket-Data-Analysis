import asyncio
from pyppeteer import launch

async def main(website):
        browser = await launch()
        page = await browser.newPage()
        await page.goto(website)
        await asyncio.sleep(3)
        html = await page.content()
        await browser.close()
        return html

website = '/records/team/team-series-results/india-6/twenty20-internationals-3'

result = asyncio.get_event_loop().run_until_complete(main('https://www.espncricinfo.com'+website))
open('T20 Scraping\T20s.html','w').write(result)
