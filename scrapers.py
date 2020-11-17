from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def al_data_title_scraper():
    al_data = urlopen('https://www.al.com/')
    al_soup = BeautifulSoup(al_data, 'html.parser')
    articles = al_soup.find_all('article')
    regex_pattern = r'\d+[hm]\sago'
    titles = []
    
    for i in articles:
        titles.append(i.text)
        
    titles = [x.strip(regex_pattern).lstrip().rstrip() for x in titles]
    titles = [i for i in set(titles)]
    
    return titles

def fox_10_news_scraper():
    fox_10_news = urlopen('https://www.fox10tv.com/')
    fox_10_news_soup = BeautifulSoup(fox_10_news, 'html.parser')
    fox_titles = fox_10_news_soup.find_all('a', class_='tnt-asset-link')
    remove_list = ['Tracking the Tropics', '1st & 10','COVID-19 Headlines', 'Back to School', 'News Now Update', 'Our Apps', 'News Now Livestream']
    regex_pattern = r'\d:\d\d'
    
    local_fox_titles = []
    for i in fox_titles:
        local_fox_titles.append(i.text.rstrip().lstrip())
        
    final_fox_titles = []
    for i in local_fox_titles:
        if i == '' or re.match(regex_pattern, i):
            pass
        elif i in remove_list:
            pass
        else:
            final_fox_titles.append(i)
            
    return list(set(final_fox_titles))

def wbrc_scraper():
    wbrc_birmingham = urlopen('https://www.wbrc.com/')
    wbrc_soup = BeautifulSoup(wbrc_birmingham, 'html.parser')
    new_titles = wbrc_soup.find_all('a',class_='unstyled-link')
    
    cleaned_titles = []
    
    for i in new_titles:
        cleaned_titles.append(i.text.rstrip().lstrip())
        
    return list(set(cleaned_titles))

def al_birmingham_scraper():
    al_birmingham = urlopen('https://www.al.com/birmingham/')
    al_soup = BeautifulSoup(al_birmingham, 'html.parser')
    articles = al_soup.find_all('article')

    for i in articles:
        regex_pattern = r'\d+[hm]\sago'
        titles = []
    
        for i in articles:
            titles.append(i.text)
        
        titles = [x.strip(regex_pattern).lstrip().rstrip() for x in titles]
        titles = [i for i in set(titles)]
    
        return titles
    
def whnt_scraper():
    whnt = urlopen('https://www.whnt.com/')
    whnt_soup = BeautifulSoup(whnt, 'html.parser')
    articles = whnt_soup.find_all(class_='article-list__article-title')

    titles = []
    for i in articles:
        titles.append(i.text.lstrip().rstrip())
    
    return list(set(titles))

def wsb_tv2_scraper():

    wsb_tv2 = urlopen('https://www.wsbtv.com/')
    wsb_tv2_soup = BeautifulSoup(wsb_tv2,'html.parser')
    articles = wsb_tv2_soup.find_all(class_='unstyled-link')

    titles = []

    for i in articles:
        titles.append(i.text.rstrip().lstrip())
    
    return titles

def nbc_dc_news_scraper():
    ### NBC Washington D.C.
    wdc_nbc4 = urlopen('https://www.nbcwashington.com/')
    wdc_nbc4_soup = BeautifulSoup(wdc_nbc4, 'html.parser')
    articles = wdc_nbc4_soup.find_all(class_='story-card__title')
    titles = []
    
    for i in articles:
        print(i.text.rstrip().lstrip())
        
    return titles

def wdc_fox_scraper():
    wdc_fox = urlopen('https://www.fox5dc.com/')
    wdc_soup = BeautifulSoup(wdc_fox, 'html.parser')
    articles = wdc_soup.find_all('article')

    titles = []

    for i in articles:
        print(re.sub('\d\d\shours\sago','',i.text).rstrip().lstrip())
        
    return titles