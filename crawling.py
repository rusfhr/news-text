import requests
import re
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "article"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (
               id INT AUTO_INCREMENT PRIMARY KEY,
               title VARCHAR(255),
               content TEXT,
               url VARCHAR(255),
               publish_date DATE
               )
               """
)

def fetch_naver_news(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # 제목과 본문 추출
    title = soup.find("h2", {"class" : "media_end_head_headline"}).get_text(strip=True)
    content = soup.find("article", {"class" : "go_trans _article_content"}).get_text(strip=True)
    publish_date_str = soup.find("span", {"class" : "media_end_head_info_datestamp_time _ARTICLE_DATE_TIME"}).get_text(strip = True)

    # 날짜 형식 변환
    publish_date = datetime.strptime(publish_date_str, "%Y.%m.%d. %p %I:%M").date()  # 날짜 형식에 맞게 조정

    return title, content, url, publish_date.date()

# MySQL에 데이터 저장
def save_news_to_db(title, content, url, publish_date):
    insert_query = """
    INSERT INTO naver_news (title, content, url, publish_date)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (title, content, url, publish_date))
    conn.commit()

# 뉴스 URL 지정
news_url = "https://n.news.naver.com/mnews/article/005/0001735722"

# 뉴스 데이터 크롤링 및 MySQL 적재
title, content, url, publish_date = fetch_naver_news(news_url)
save_news_to_db(title, content, url, publish_date)

print("뉴스 데이터가 성공적으로 저장되었습니다.")

# 연결 종료
cursor.close()
conn.close()