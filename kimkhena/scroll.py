import json
import time
import sys

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# 셀레눔 드라이버와 스크롤 횟수를 받아서 스크롤을 내리는 함수 
def scroll_page(driver, scroll_count):  # 스크롤 횟수만큼 스크롤을 내림
    # 지금의 스크롤 길이
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(scroll_count):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
    
        # 새로운 스크롤 길이 기록
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break  # 더 이상 스크롤할 내용이 없으면 멈춤
        last_height = new_height


# BeautifulSoup로 리뷰를 추출하는 함수
def extract_reviews(html):
    soup = BeautifulSoup(html, 'html.parser')

    #리뷰 저장 딕셔너리들
    reviews = []
    ratings = []
    review_list = []


    #모든 리뷰글 찾기
    text_container = soup.find_all('p', class_='content-text css-c92dc4')
    #리뷰글 딕셔너리에 넣기
    for text in text_container:
        review_text =text.text.replace("\n"," ")
        reviews.append(review_text)


    #모든 리뷰 추출
    review_item_container = soup.find_all('div', class_='review-item-container')

    #모든 별점 찾기
    for container in review_item_container:
        #5개 별 찾기
        rating_container = container.find('div', class_='css-rz7kwu')
        #1개 별 찾기
        stars = rating_container.find_all('svg', class_='css-1mhwecd')

        #별점 카운트
        review_rating =0

        for star in stars:
            # 별의 테두리와 색이 있는지 찾기
            rating = star.find_all('path')

            #별이 채워져 있다면 review_rating 1 추가
            if len(rating) == 2:
                review_rating+=1
        
        #별점 딕셔너리에 추가
        ratings.append(review_rating)
    review_list = [{ "리뷰": reviews[i], "별점": ratings[i] } for i in range(len(reviews))]
    return review_list


# 리뷰를 엑셀로 저장하는 함수
def save_reviews(name, review_list): 
    #데이터프레임으로 변환
    df = pd.DataFrame(review_list)
    #엑셀 파일로 이름
    filename = f"{name}_reviews.xlsx"\
    #엑셀 파일 저장 
    df.to_excel(filename, index=False)
    return filename
    

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
    name="서울 웨스틴조선호텔"
    url="https://www.yanolja.com/reviews/domestic/1000108384"
    crawl_yanolja_reviews(name=name, url=url)

print("done")
