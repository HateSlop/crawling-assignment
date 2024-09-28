# Section3. 웹크롤링이란?

## 웹크롤링의 개념과 활용 사례

 > 웹크롤링: 웹사이트에 있는 정보를 자동으로 빠르게 수집하는 것

 > 웹 크롤링 활용
    - 데이터 분석 과정
    - 웹사이트 자동화
    - 인공지능 학습 데이터
> 웹 페이지를 어떻게 볼 수 있을까?
- HTTP 통신: 웹 브라우저와 웹 서버 사이에 데이터를 주고 받는 데 사용되는 통신
    - 브라우저(사용자)가 서버에게 주소로(HTTP) 요청 -> 서버가 브라우저에게 HTML로 응답.

# Section4. 웹크롤링 학습 전 준비물 챙기기

## 준비물1) HTML 기초

> H1TML: Hyper Text Markup Language 
- 웹사이트 구조 표시하기 위한 언어
- 전체 구조:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- 문서의 잡다한 정보 -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title> <!--웹페이지 제목-->
</head>
<body>
    <!-- 화면에 표시되는 내용 -->
     <h1>헤딩 태그, 제목/소제목</h1>
     <div>구역을 나타내는 태그<!-- 웹페이지의 여러 구역 나타냄. 크롤링 할 때 많이 접함 -->
        <h1>구역 안쪽 제목</h1>
        <p>문단을 나타내는 태그</p>
        <a href = "이동하는 실제 주소">하이퍼링크 태그</a>
        <input type = "input으로 받을 데이터 타입">
        <button onclick="alert('팝업 내용')">버튼 만들어줌</button>
        <ul>
            <!--목록 태그-->
            <li>항목</li>
        </ul>
     </div>
</body>
</html>
```
- 태그 구조
```html
<태그 이름 속성 = "속성값"> 내용 </태그 이름>
```
- 속성: 태그의 추가적 정보
    - 여러개 부여 가능, 없어도 무방
- 내용에는 텍스트 혹은 태그 들어갈 수 있고, 없어도 무방
    - 태그 안의 태그는 자식 태그, 자식 포함하는 태그는 부모 태그

## 준비물2) CSS 선택자

> CSS: Webpage의 디자인 담당 
- 기본 문법
```css
h1/*선택자*/{/*선언 시작*/ color/*속성명*/:red;/*속성값*/ } /*선언 종료*/
```
- 선택자
    - 웹페이지에서 원하는 태그를 선택하는 문법
    - 선택자 종류
        - 1. 태그 선택자: 태그 이름으로 선택하는 것. 다른 선택자와 결합해 사용
        - 2. 클래스 선택자(가장 많이 사용됨): 클래스 속성 값으로 선택하는 것.
            - 클래스: 태그에 별명을 주는 것. 마침표(.)로 시작.
        - 3. 아이디 선택자: 아이디 속성 값으로 선택하는 것.
            - 아이디: 태그에 별명을 주는 것. #으로 시작.
        - 4. 자식 선택자: 바로 아래 자식 태그 선택하는 것. 내가 원하는 태그에 별명이 없을 떄 사용 .header > p 꼴.

- 구조
```html
    <style>
        div { background-color: steelblue; padding: 15px; margin-bottom: 20px;border-radius: 5px;}
        .sub-title {font-size: 24px;}
        #main-title { color: orange;}
        .box > p { color: lightskyblue;}        
    </style>
```

# Section5. 웹크롤링 라이브러리 사용법 마스터하기!

## requests, Beautifulsoup4 사용법 빠르게 알아보기

> 웹크롤링 기초: 정적 페이지(static page) 크롤링
- 정적 페이지: 데이터에 추가적인 변경이 일어나지 않는 페이지(응답받은 HTML에 정보다 다 들어있음)
- 과정
    - 데이터 받아오기
        - 파이썬에서 서버에 요청을 보내고 응답 받기
        - HTTP 통신으로 HTML을 받아오기
    - 데이터 뽑아내기
        - HTML에서 원하는 부분만 추출

> requests 사용법 실습
- 코드 예제
```python
import requests 
response = requests.get("https://startcoding.pythonanywhere.com/basic")
response.status_code #status_code로 응답 상태 확인. 200이면 잘 된 것.
```
```python
from bs4 import BeautifulSoup
html = response.text
soup = BeautifulSoup(html, 'html.parser')
#parser = split html into tag unit
soup.select_one("선택자")
#select_one = 해당되는 태그 중 가장 첫번째 태그를 가져옴

```
- 선택자 만드는 과정
    - F12(개발자모드) -> 좌측 상단 화살표 모양 클릭 -> 웹페이지에서 선택자 클릭하면 html파일에서 태그 뜸
    - 태그에 아이디/클래스가 있는지 확인. 아이디/클래스 더블클릭하면 복사 가능
    - 앞에 . 붙혀서 "선택자"에 복붙
    - select_one().text: 해당 태그의 텍스트 긁어옴

## 실전 크롤링 1단계: 한개의 상품 크롤링 하는 법
> 코드 예제

```python
category = soup.select_one(".product-category").text
name = soup.select_one(".product-name").text
link = soup.select_one(".product-name > a").attrs["href"]
price = soup.select_one(".product-price").text.strip().replace(',','').replace('원','')
#strip(): 앞뒤 공백 제거, replace('A','B'): A를 B로 변환
print(category)
print(name)
print(link)
print(price)
#노트북
#에이서 스위프트 GO 16 OLED, 스틸 그레이, 코어i7, 512GB, 16GB, WIN11 Home, SFG16-71-77FT
##product1_detail.html
#1419000
```

## 실전 크롤링 2단계: 여러개의 상품 크롤링 하는 법 [포레스트 이론]

> 포레스트 이론
- 숲: 페이지 전체 HTML
- 나무: 원하는 정보를 모두 담는 태그

> 과정
- 나무 찾기: 웹페이지에서 내가 원하는 정보가 모두 담긴 태그 찾기.
- CSS 선택자 만들기
- select()메서드로 나무 뽑기
    - select(): 선택자에 매칭되는 태그 전체를 리스트로 반환
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

## 실전 크롤링 3단계: 어러개의 페이지 크롤링 하는 법 [URL 조작자]

> URL(Uniform Resource Locator)
- 인터넷 주소 형식
- 프로토콜 - 도메인 - 경로 - 파라미터(서버에 추가적인 정보 제공)
- https(protocol)://domain/path?key=value(parameter)
- 코드 예제
```python
for i in range(1, 5):
    response = requests.get(f"https://startcoding.pythonanywhere.com/basic?page={i}")
```

## 실전 크롤링 4단계: 크롤링한 데이터 엑셀에 저장하는 법

> pandas, openpyxl

> 과정: 
- 1. 비어있는 리스트를 만들고 데이터를 한 행 씩 추가
- 2. pandas로 데이터프레임 만들고 엑셀로 저장



