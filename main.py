import scrapers as sc
from db import dbctrl as dbc

def run_all():
    al_headlines_main = sc.al_data_title_scraper()
    dbc.add_headlines(al_headlines_main, 'https://www.al.com')
    fox_10_headlines = sc.fox_10_news_scraper()
    dbc.add_headlines(fox_10_headlines, 'https://www.fox10tv.com')
    wbrc_headlines = sc.wbrc_scraper()
    dbc.add_headlines(wbrc_headlines, 'https://www.wbrc.com/')
    birmingham_al = sc.al_birmingham_scraper()
    dbc.add_headlines(birmingham_al, 'https://www.al.com/birmingham/')
    huntsville_news = sc.whnt_scraper()
    dbc.add_headlines(huntsville_news, 'https://www.whnt.com/')
    wsb_tv2 = sc.wsb_tv2_scraper()
    dbc.add_headlines(wsb_tv2, 'https://www.wsbtv.com/') 
    nbc_dc = sc.nbc_dc_news_scraper()
    dbc.add_headlines(nbc_dc, 'https://www.nbcwashington.com/')    
    wdc_fox = sc.wdc_fox_scraper()
    dbc.add_headlines(wdc_fox, 'https://www.fox5dc.com/')
    
    return 'Program has sucessfully scraped and saved the data.'