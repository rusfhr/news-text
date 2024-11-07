from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = '/Users/kang-gyeongrok/Desktop/Visual Studio Code/chromedriver'

options = Options()
# options.add_argument("--headless")  # 브라우저를 표시하지 않고 실행
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# ChromeDriver 서비스 설정
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service = service, options = options)

url = 'https://news.naver.com'

driver.get(url)

time.sleep(2)

driver.find_element(By.XPATH, '/html/body/section/header/div[2]/div/div/div/div/div/ul/li[2]/a').click()
time.sleep(2)










driver.quit()