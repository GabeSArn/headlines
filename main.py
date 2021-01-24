import scrapers as sc
from db import dbctrl as dbc

def run_all():
    al_headlines_main = sc.al_data_title_scraper()
    dbc.add_headlines(al_headlines_main, 'https://www.al.com')
    
    ### Mobile, Al
    fox_10_headlines = sc.fox_10_news_scraper()
    dbc.add_headlines(fox_10_headlines, 'https://www.fox10tv.com')
    wbrc_headlines = sc.wbrc_scraper()
    dbc.add_headlines(wbrc_headlines, 'https://www.wbrc.com/')
    
    ### Birmingham, AL
    birmingham_al = sc.al_birmingham_scraper()
    dbc.add_headlines(birmingham_al, 'https://www.al.com/birmingham/')
    
    ### Huntsville, AL
    huntsville_news = sc.whnt_scraper()
    dbc.add_headlines(huntsville_news, 'https://www.whnt.com/')
    
    ### Atlanta, GA
    wsb_tv2 = sc.wsb_tv2_scraper()
    dbc.add_headlines(wsb_tv2, 'https://www.wsbtv.com/')
    
    ### Washington, D.C.
    nbc_dc = sc.nbc_dc_news_scraper()
    dbc.add_headlines(nbc_dc, 'https://www.nbcwashington.com/')
    wdc_fox = sc.wdc_fox_scraper()
    dbc.add_headlines(wdc_fox, 'https://www.fox5dc.com/')
    
    ### Houston, Texas
    abc13_houston = sc.abc13_houston_scraper()
    dbc.add_headlines(abc13_houston, 'https://abc13.com/houston/')
    khou_houston = sc.khou_houston_scraper()
    dbc.add_headlines(khou_houston, 'https://www.khou.com/texas')
    fox26_houston = sc.fox26_houston_scraper()
    dbc.add_headlines(fox26_houston, 'https://www.fox26houston.com/news')
    click2_houston = sc.click2_houston_scraper()
    dbc.add_headlines(click2_houston, 'https://www.click2houston.com/news/')
    
    ### Los Angeles, CA
    abc7_la = sc.abc7_la_scraper()
    dbc.add_headlines(abc7_la, 'https://abc7.com/los-angeles/')  
    nbc4_la = sc.nbc4_la_scraper()
    dbc.add_headlines(nbc4_la, 'https://www.nbclosangeles.com/')  
    ktla = sc.ktla_scraper()
    dbc.add_headlines(ktla, 'https://ktla.com/news/')
    foxla = sc.foxla_scraper()
    dbc.add_headlines(foxla, 'https://www.foxla.com/news')
    
    ### New York City NY
    nyc_abc7 = sc.nyc_abc7_scraper()
    dbc.add_headlines(nyc_abc7, 'https://abc7ny.com/new-york/')
    
    ### San Francisco, CA
    abc7_news_sf = sc.abc7_news_sf_scraper()
    dbc.add_headlines(abc7_news_sf, 'https://abc7news.com/')
    
    ### Seattle, WA
    king5 = sc.king5_scraper()
    dbc.add_headlines(king5, 'https://www.king5.com/')
    
    
    
    
    
    return 'Program has sucessfully scraped and saved the data.'