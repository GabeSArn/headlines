import sqlite3
import datetime
from datetime import date
import pandas as pd

def db_details():
    con = sqlite3.connect('news.db')
    cursor = con.cursor()
    info = cursor.execute('SELECT COUNT(titles) from news_titles')
    info = info.fetchone()
    return info

def show_all_data():
    con = sqlite3.connect('news.db')
    cursor = con.cursor()
    cursor.execute('SELECT * from news_titles')
    titles = cursor.fetchall()
    con.close()
    return titles

def grab_titles():
    title_list = []
    dirty_data = pd.Series(show_headlines())
    for i in dirty_data:
        title_list.append(i[0])
    return pd.Series(title_list)

def show_headlines():
    con = sqlite3.connect('news.db')
    cursor = con.cursor()
    cursor.execute('SELECT article_title from news_titles')
    titles = cursor.fetchall()
    con.close()
    return titles

def add_headlines(titles, source):
    today = date.today()
    weekday = 'Monday'
    for i in titles:
        con = sqlite3.connect('news.db')
        cursor = con.cursor()
        cursor.execute('INSERT INTO news_titles (article_title, source, weekday, date) VALUES (?,?,?,?)', (i, source, weekday, today))
        con.commit()
        
    con.close()