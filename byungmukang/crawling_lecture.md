#  웹크롤링이란?

## 웹크롤링의 개념과 활용 사례

 - 웹크롤링: 웹사이트에서 자동으로 데이터를 수집하는 프로세스

 - 웹 크롤링 활용
     + 데이터 분석 과정
     + 웹사이트 자동화
     + 인공지능 학습 데이터

# 웹크롤링 학습 전 준비물 챙기기

## HTML 기초

- HTML: Hyper Text Markup Language 
    + 웹 페이지의 구조와 내용을 정의하는 마크업 언어
```
<!DOCTYPE html>
<html>
<!-- HTML 문서의 시작을 알리는 선언 -->
<head>
    <!-- 문서의 메타데이터나 스타일, 스크립트 등을 정의하는 부분 -->
    <title>My First Webpage</title> <!-- 브라우저 탭에 표시될 제목 -->
</head>
<body>
    <!-- 실제 웹 페이지에 표시되는 내용이 들어가는 부분 -->
    <h1>Welcome to My Website</h1> <!-- 가장 큰 제목을 나타내는 태그 -->
    <p>This is a paragraph of text on my first webpage.</p> <!-- 단락을 나타내는 태그 -->
    <a href="https://www.example.com">Click here to visit Example</a> <!-- 다른 웹 페이지로 이동하는 링크 -->
</body>
</html>

```
- 태그 구조
```html
<태그 이름 속성 = "속성값"> 내용 </태그 이름>
```


##  CSS 

  - CSS: 웹 페이지의 스타일과 레이아웃을 정의하는 언어
```css
/* h1 태그의 스타일 */
h1 {
    color: blue; /* 글자 색상을 파란색으로 */
    font-size: 36px; /* 글자 크기를 36px로 */
    text-align: center; /* 텍스트를 가운데 정렬 */
}

/* p 태그의 스타일 */
p {
    font-family: Arial, sans-serif; /* 글꼴을 Arial로 설정 */
    font-size: 18px; /* 글자 크기를 18px로 설정 */
    color: gray; /* 글자 색상을 회색으로 */
    line-height: 1.6; /* 줄 간격을 1.6으로 설정 */
}

/* a 태그(링크)의 스타일 */
a {
    color: green; /* 링크 색상을 녹색으로 */
    text-decoration: none; /* 링크 밑줄 제거 */
}

a:hover {
    color: red; /* 링크에 마우스를 올렸을 때 색상을 빨간색으로 변경 */
}

```

# 웹크롤링 라이브러리 사용법 마스터하기!

## requests, Beautifulsoup4 사용법 빠르게 알아보기

- 정적 페이지: 사용자와의 상호작용 없이 고정된 콘텐츠를 제공하는 웹 페이지

- 코드 예제
```python
import requests 
response = requests.get("https://startcoding.pythonanywhere.com/basic")
response.status_code 
```
```python
from bs4 import BeautifulSoup
html = response.text
soup = BeautifulSoup(html, 'html.parser')
#parser = split html into tag unit
soup.select_one("선택자")
```
## 선택자 만드는 방법

1. **개발자 도구 열기**
   - `F12` 키로 개발자 도구

2. **요소 선택 도구 사용**
   - 좌측 상단 화살표 모양 클릭 → 선택할 요소를 웹 페이지에서 클릭.

3. **HTML 코드에서 태그 확인**
   - 선택한 요소의 HTML 태그 확인.

4. **ID 또는 클래스 확인**
   - `id` 또는 `class` 속성이 있는지 확인.
   - 더블 클릭으로 ID/클래스 복사.

5. **CSS 선택자 생성**
   - `id` → 앞에 `#` 붙이기 (예: `#myId`)
   - `class` → 앞에 `.` 붙이기 (예: `.myClass`)

6. **선택자 사용**
   - `select_one('선택자').text`로 해당 태그의 텍스트 추출.


## 실전 크롤링 1단계: 한 개의 상품 크롤링 하는 법
```python
category = soup.select_one(".product-category").text
name = soup.select_one(".product-name").text
link = soup.select_one(".product-name > a").attrs["href"]
price = soup.select_one(".product-price").text.strip().replace(',','').replace('원','')
print(category)
print(name)
print(link)
print(price)
#노트북
#에이서 스위프트 GO 16 OLED, 스틸 그레이, 코어i7, 512GB, 16GB, WIN11 Home, SFG16-71-77FT
##product1_detail.html
#1419000
```

## 실전 크롤링 2단계: 여러개의 상품 크롤링 하는 법

- 코드 예제
```python
items = soup.select(".product")
for item in items:
    category = item.select_one(".product-category").text
    name = item.select_one(".product-name").text
    link = item.select_one(".product-name > a").attrs["href"]
    price = item.select_one(".product-price").text.split('원')[0].replace(',','')
    #split('원'): '원'을 기준으로 자르기 한 후 앞부분만 가져오기
    print(category)
    print(name)
    print(link)
    print(price)
```

## 실전 크롤링 3단계: 여러 개의 페이지 크롤링 


- 코드 예제
```python
for i in range(1, 5):
    response = requests.get(f"https://startcoding.pythonanywhere.com/basic?page={i}")
```

## 실전 크롤링 4단계: 크롤링한 데이터 엑셀에 저장하는 법


1. 비어있는 리스트를 만들고 데이터를 한 행 씩 추가
2. pandas로 데이터프레임 만들고 엑셀로 저장


