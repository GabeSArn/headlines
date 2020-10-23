import scrapers as sc
from db import dbctrl as dbc

def run_all():
    al_headlines_main = sc.al_data_title_scraper()
    dbc.add_headlines(al_headlines_main, 'www.al.com')
    fox_10_headlines = sc.fox_10_news_scraper()
    dbc.add_headlines(fox_10_headlines, 'www.fox10tv.com')
    wbrc_headlines = sc.wbrc_scraper()
    dbc.add_headlines(wbrc_headlines, 'www.wbrc.com/')
    birmingham_al = sc.al_birmingham_scraper()
    dbc.add_headlines(al_birmingham_scraper(), 'https://www.al.com/birmingham/')
    huntsville_news = sc.whnt_scraper()
    dbc.add_headlines(huntsville_news, 'https://www.whnt.com/')
        
    return 'Program has sucessfully scraped and saved the data.'