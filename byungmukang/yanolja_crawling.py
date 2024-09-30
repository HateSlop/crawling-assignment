import json
import time
import sys
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# 셀레눔 드라이버와 스크롤 횟수를 받아서 스크롤을 내리는 함수 
def scroll_page(driver, scroll_count):  # 스크롤 횟수만큼 스크롤을 내림
    for _ in range(scroll_count):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)

# BeautifulSoup로 리뷰를 추출하는 함수
def extract_reviews(html):
    soup = BeautifulSoup(html, 'html.parser')
    reviews = []

    # 리뷰 컨테이너 찾기 (class명은 실제 HTML 구조에 맞게 변경해야 할 수 있음)
    review_containers = soup.find_all('div', class_='review-item-container')

    for container in review_containers:
        # 별점 추출
        star_container = container.find('div', class_='css-rz7kwu')
        if star_container:
            stars = star_container.find_all('svg', class_='css-1mhwecd')
            star_rating = len(stars)
        else:
            star_rating = 0

        # 리뷰 내용 추출
        review_text_tag = container.find('p', class_='content-text')
        if review_text_tag:
            review_text = review_text_tag.get_text(strip=True)
        else:
            review_text = ''

        # 리뷰와 별점을 딕셔너리 형태로 저장
        reviews.append({
            '별점': star_rating,
            '리뷰': review_text
        })

    return reviews

# 리뷰를 엑셀로 저장하는 함수
def save_reviews(name, review_list):
    # 데이터프레임으로 변환
    df = pd.DataFrame(review_list)

    # 엑셀 파일로 저장 (encoding 파라미터 제거)
    filename = f"{name}_reviews.xlsx"
    df.to_excel(filename, index=False)
    print(f"Reviews saved to {filename}")


def crawl_yanolja_reviews(name, url):
    # 드라이버 
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)

    # 스크롤 횟수
    scroll_count = 5
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
    name = "파주 메이트 호텔"
    url = "https://www.yanolja.com/reviews/domestic/3001541"
    crawl_yanolja_reviews(name=name, url=url)
