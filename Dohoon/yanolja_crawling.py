import json
import time
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


# 셀레눔 드라이버와 스크롤 횟수를 받아서 스크롤을 내리는 함수 
def scroll_page(driver, scroll_count):  # 스크롤 횟수만큼 스크롤을 내림
    for _ in range(scroll_count):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)


# BeautifulSoup로 리뷰를 추출하는 함수
def extract_reviews(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    items = soup.select(".review-item-container")
    
    for item in items:
        count = 0
        for svg in item.select("svg"):
            if svg.find('path', {'fill': '#FDBD00'}):
                count += 1
        review = item.select_one(".content-text.css-c92dc4").text
        data.append([count, review])
    
    return data


# 리뷰를 엑셀로 저장하는 함수
def save_reviews(name, review_list): 
    df = pd.DataFrame(review_list, columns = ['point', 'review'])
    df.to_excel(f"yanolja_review_{name}.xlsx", index=True)    
    return
    

def crawl_yanolja_reviews(name, url):
    # 드라이버 
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    # 스크롤 횟수
    scroll_count = 20
    # 스크롤 내리기 함수 실행
    scroll_page(driver, scroll_count)

    # 리뷰 추출
    html = driver.page_source
    # 리뷰 추출 함수 실행
    review_list = extract_reviews(html)

    # 리뷰 저장 함수 실행 
    save_reviews(name, review_list)
    driver.quit()

if __name__ == '__main__':
    name="L7해운대"
    url="https://www.yanolja.com/reviews/domestic/10057260"
    crawl_yanolja_reviews(name=name, url=url)