import requests
from bs4 import BeautifulSoup
import mysql.connector

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "review"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movie-reviews (
               id INT AUTO_INCREMENT PRIMARY KEY,
               movie_title VARCHAR(256),
               review_text TEXT,
               review_score INT,
               review_date DATE
               )
               """
)

def get_movie_review(movie_id, pages = 1):
    reviews = []
    for page in range(1, pages + 1):
        url = f""