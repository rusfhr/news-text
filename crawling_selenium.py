from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = '/Users/kang-gyeongrok/Desktop/Visual Studio Code/chromedriver'

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service = service, options = options)

url = 'https://n.news.naver.com/mnews/article/005/0001735722'

driver.get(url)

time.sleep(2)

try:
    title = driver.find_element(By.CLASS_NAME, 'media_end_head_headline').text
    content = driver.find_element(By.CLASS_NAME, 'go_trans._article_content').text

    print('제목 : ', title)
    print('\n본문 : ', content)

except Exception as e:
    print('오류 발생', e)

driver.quit()