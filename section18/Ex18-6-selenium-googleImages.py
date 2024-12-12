'''
파일명: Ex18-6-selenium-googleImages

selenium 패키지
    어플리케이션 테스트하기 위한 프레임웍 이다.
    웹 어플리케이션 다양한 브라우저 동작 테스트용!
    웹 크롤링으로 많이 사용된다.


# 브라우저 컨트롤 패키지
pip install selenium
# selenium에서 사용하는 브라우저 드라이버 자동관리 도구
pip install webdriver-manager

'''

import os
import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager



# Chrome driver 자동 설치 및 서비스 생성
service = Service(ChromeDriverManager().install())

# Chrome 드라이버 인스턴스 생성
driver = webdriver.Chrome(service=service)

# 드라이버를 통해 Google 페이지 접속
driver.get("https://images.google.com/")

# 키워드
keyword = 'cute cat'

# 검색어 입력
searh_bar = driver.find_element(By.NAME, 'q')
searh_bar.send_keys(keyword)
searh_bar.send_keys(Keys.RETURN)

time.sleep(2)

thumnails = driver.find_elements(By.CSS_SELECTOR, '.H8Rx8c')

print(len(thumbnails))

thumnails[0].click()

time.sleep(2)

#sFlh5c FyHeAf iPVvYb

image = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.sFlh5c.FyHeAf.iPVvYb')
    )
)

# 이미지 URL 가져오기
image_url = image.get_attribute('src')

print(f'image_url: {image_url}')

time.sleep(3000)



# 드라이버 종료
driver.quit()

#shift enter하면 여러 줄 쓰기가능 , ctrl 마우스 클릭해서 모듈을 자세히 볼 수 있다





















