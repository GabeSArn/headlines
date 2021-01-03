from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def al_data_title_scraper():
    ### Alabama
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
    ### Mobile, Alabama
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
    ### Birmingham, Al
    wbrc_birmingham = urlopen('https://www.wbrc.com/')
    wbrc_soup = BeautifulSoup(wbrc_birmingham, 'html.parser')
    new_titles = wbrc_soup.find_all('a',class_='unstyled-link')
    
    cleaned_titles = []
    
    for i in new_titles:
        cleaned_titles.append(i.text.rstrip().lstrip())
        
    return list(set(cleaned_titles))

def al_birmingham_scraper():
    ### Birmingham, Al
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
    ### Huntsville, Al
    whnt = urlopen('https://www.whnt.com/')
    whnt_soup = BeautifulSoup(whnt, 'html.parser')
    articles = whnt_soup.find_all(class_='article-list__article-title')

    titles = []
    for i in articles:
        titles.append(i.text.lstrip().rstrip())
    
    return list(set(titles))

def wsb_tv2_scraper():
    ### Atlanta, GA
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
        titles.append(i.text.rstrip().lstrip())
        
    return titles

def wdc_fox_scraper():
    ### Washington D.C.
    wdc_fox = urlopen('https://www.fox5dc.com/')
    wdc_soup = BeautifulSoup(wdc_fox, 'html.parser')
    articles = wdc_soup.find_all('article')

    titles = []

    for i in articles:
        titles.append(re.sub('\d\d\shours\sago','',i.text).rstrip().lstrip())
        
    return titles

def abc13_houston_scraper():
    ### Houston, Tx
    abc13_houston = urlopen('https://abc13.com/houston/')
    abc13_houston_soup = BeautifulSoup(abc13_houston, 'html.parser')
    articles = abc13_houston_soup.find_all(class_='headline')

    result = list(set([i.text for i in articles if i.text != '']))

    return result

def khou_houston_scraper():
    ### Houston, Tx
    khou_houston = urlopen('https://www.khou.com/texas')
    khou_houston_soup = BeautifulSoup(khou_houston, 'html.parser')
    articles = khou_houston_soup.find_all(class_='headline-list__title')

    result = [i.text for i in articles if i.text != '']

    return result

def fox26_houston_scraper():
    ### Houston, Tx
    fox26_houston = urlopen('https://www.fox26houston.com/news')
    fox26_houston_soup = BeautifulSoup(fox26_houston, 'html.parser')
    articles = fox26_houston_soup.find_all(class_='title')

    result = [i.text for i in articles if i.text != '' and i.text != 'News' and i.text != 'Latest Local News' and i.text != '\n        Latest News\n      ']

    return result

def click2_houston_scraper():
    ### Houston, Tx
    click2_houston = urlopen('https://www.click2houston.com/news/')
    click2_houston_soup = BeautifulSoup(click2_houston, 'html.parser')
    articles = click2_houston_soup.find_all(class_='no-margin')

    result = [i.text for i in articles if i.text != '' and i.text != 'NewsSportsThings To DoFind Your CityDiscoverHouston LifeWeatherTrafficNewsletters']
    result = list(set(result))
    
    return result

def nyc_abc7_scraper():
    ### Houston, Tx
    nyc_abc7 = urlopen('https://abc7ny.com/new-york/')
    nyc_soup = BeautifulSoup(nyc_abc7, 'html.parser')
    articles = nyc_soup.find_all(class_='headline')

    articles = [i.text for i in articles]
    
    return articles

def nyc_abc7_scraper():
    ### New York City, NY
    nyc_abc7 = urlopen('https://abc7ny.com/new-york/')
    nyc_soup = BeautifulSoup(nyc_abc7, 'html.parser')
    articles = nyc_soup.find_all(class_='headline')

    articles = [i.text for i in articles]
    
    return articles

def abc7_la_scraper():
    ### Los Angeles, CA
    abc7_la = urlopen('https://abc7.com/los-angeles/')
    abc7_soup = BeautifulSoup(abc7_la, 'html.parser')
    articles = abc7_soup.find_all(class_='headline')

    articles = [i.text for i in articles if i.text != '']
    
    return articles

def nbc4_la():
    ### Los Angeles, CA
    nbc4_la = urlopen('https://www.nbclosangeles.com/')
    nbc4_soup = BeautifulSoup(nbc4_la, 'html.parser')
    articles = nbc4_soup.find_all('a', class_='story-card__title-link')
    
    articles = [i.text.replace('\n', '').replace('\t','') for i in articles]
    
    return articles

def ktla():
    ### Los Angeles, CA
    ktla = urlopen('https://ktla.com/news/')
    ktla_soup = BeautifulSoup(ktla, 'html.parser')
    articles = ktla_soup.find_all(class_='article-list__article-title')

    articles = [i.text.replace('\n', '').replace('\t','') for i in articles]
    
    return articles

def foxla():
    ### Los Angeles, CA
    foxla = urlopen('https://www.foxla.com/news')
    foxla_soup = BeautifulSoup(foxla, 'html.parser')
    articles = foxla_soup.find_all(class_='title')


    articles = [i.text.replace('\n', '') for i in articles if i.text != 'News' or i.text != 'Latest Local News']

    articles.remove('News')
    articles.remove('Latest Local News')

    return articles

def king5():
    ### Seattle, WA
    king5 = urlopen('https://www.king5.com/')
    king5_soup = BeautifulSoup(king5, 'html.parser')
    articles = king5_soup.find_all('a', class_='headline-list__title')

    articles = [i.text for i in articles]

    return articles

def abc7_news_sf():
    ### San Francisco, CA
    abc7_news_sf = urlopen('https://abc7news.com/')
    abc7_news_soup = BeautifulSoup(abc7_news_sf, 'html.parser')
    articles = abc7_news_soup.find_all('div', class_='headline')

    articles = [i.text for i in articles]

    return articles



