from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
import re

# Seleminum으로 웹페이지를 로드한다.
driver = webdriver.Chrome()
driver.get('https://www.yanolja.com/reviews/domestic/10041505')
time.sleep(3) # 페이지 로딩 기다리기

# 스크롤 횟수 설정
scroll_count = 10
for _ in range(scroll_count):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1) # 스크롤 이후 대기


# 웹페이지 소스를 가져온다.
page_source = driver.page_source

# BeautifulSoup를 사용해 HTML을 파싱한다.
soup = BeautifulSoup(page_source, 'html.parser')

# 별점을 추출한다.
ratings = []
rating_containers = soup.find_all('div', class_='css-rz7kwu')

for container in rating_containers:
    stars = container.find_all('svg', class_='css-1mhwecd')
    
    rating = 0
    for star in stars:
        if star.find('path', fill='#FDBD00'): # 채워진 별인지 확인
            rating += 1
    ratings.append(rating)

# 리뷰 텍스트를 추출한다.
reviews_class = soup.find_all(class_= 'content-text css-c92dc4')
reviews = []

for review in reviews_class:
    # 리뷰 텍스트 정리 후 리스트에 추가
    cleaned_text = review.get_text(strip=True).replace('\r', '').replace('\n', '')
    reviews.append(cleaned_text)

# 드라이버를 종료한다.
driver.quit()

data = list(zip(ratings, reviews)) # 별점, 리뷰 결합한 리스트 생성

# DataFrame으로 변환
df_reviews = pd.DataFrame(data, columns=['Rating', 'Review'])

# 과제 외 추가 구현

# 추출한 별점의 평균 계산
average_rating = sum(ratings) / len(ratings) if ratings else 0

# 리뷰에 자주 등장하는 단어 추출
korean_stopwords = set(['이', '그', '저', '것', '들', '다', '을', '를', '에', '의', '가', '이', '는', '해', '한', '하', '하고', '에서', '에게', '과', '와', '너무', '잘', '또','좀', '호텔', '아주', '진짜', '정말'])
all_reviews_text = ' '.join(reviews)  # 모든 리뷰를 하나의 문자열로 결합
words = re.findall(r'\b\w+\b', all_reviews_text) # 특수문자 제거
filtered_words = [word for word in words if word not in korean_stopwords] # 불용어 제거
word_counts = Counter(filtered_words) # 단어 빈도 계산
common_words = word_counts.most_common(15)

summary_df = pd.DataFrame({
    'Average Rating': [average_rating],
    'Common Words': [', '.join([f"{word}({count})" for word, count in common_words])]
})

# 최종 결과
final_df = pd.concat([df_reviews, summary_df], ignore_index=True)
final_df.to_excel('yanolja_reviews.xlsx', index=False)