# -*- coding: utf-8 -*-
# CrawlingFinancialNews.py
import requests
from bs4 import BeautifulSoup
import os
import telegram
import time
from datetime import datetime

# 토큰을 지정해서 bot을 선언해 줍시다! (물론 이 토큰은 dummy!)
bot = telegram.Bot(token='725512368:AAG9b6iK9L7FYdFzdUIWs2pVcETUoWHabo8')
chat_id = bot.getUpdates()[-1].message.chat.id

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

server_link = 'https://finance.naver.com/'


#req.encoding = 'utf-8' # Clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가해줘야합니다.

while True:
    req = requests.get(server_link)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.select('span > a')
    href = soup.select('span > a')[0]['href']
    # for post in posts:
    #     print(post)

    #latest_text = posts[0].text.encode('utf8')
    latest_text = posts[0].text
    #latest_href = server_link + '/' + href.encode('utf8')
    latest_href = server_link + '/' + href

    latest = latest_text + 'Link :' + latest_href

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
        before = f_read.readline()
        if before != latest:
            bot.sendMessage(chat_id=chat_id, text=latest)
            with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
                f_write.write(latest)
                f_write.close()
        # else:
        #     bot.sendMessage(chat_id=chat_id, text='No Information')
        f_read.close()

    now = datetime.now()
    print('Time : ' + '%s-%s-%s-%s-%s-%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second) + 'Content : ' + latest)
    time.sleep(600)


#content > div.article > div.section > div.news_area > div > ul > li:nth-child(1) > span > a