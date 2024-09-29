# 이것이 진짜 크롤링이다 - 기본편
## 내 컴퓨터에서 파이썬 동작시키기(환경설정)

**Python** - 소스 코드를 해석하고 실행하기 위한 프로그램   
**Visual studio code(vs code)** - 소스 코드를 작성할 때 편한 기능들을 제공하는 프로그램   
**주피터 노트북(jupter Notebook)** - 셀 단위로 실행할 수 있는 편집 프로그램 / 데이터를 각 셀마다 확인 가능   

## 웹크롤링의 개념과 활용사례
**웹크롤링(Web Crawling)** - 웹사이트에 있는 정보를 자동으로 빠르게 수집하는 것   
웹크롤링의 활용 - 데이터 수집 / 웹사이트 자동화 / 인공지능 학습 데이터
활용 사례   
1. 상품 컨텐츠 자동 업로드
2. 부동산 주식 재테크 데이터 수집
3. 인스타그림, 유튜브 모니터링 및 분석
4. 뉴스 데이터 수집
5. 논문, 구인공고 데이터 수집

**HTTP 통신** - 웹 브라우저와 웹 서버 사이에 데이터를 주고 받는데 사용되는 통신   
사용자의 요청을 웹 서버는 HTML(페이지에 대한 정보)로 응답   

## HTML 기초
웹사이트 개발의 3요소   
1. **HTML(Hyper Text Markup Language)** - 웹사이트의 구조를 표시하기 위한 언어
2. **CSS** - 디자인
3. **JavaScript** - 동작
```
<태그이름 속성="속성갑"> 내용 </태그이름>   
<!--주석처리-->
```
속성 - 태그의 추가적인 정보 / 여러개 들어갈 수도 하나도 안 들어갈 수도 있음   
```
<head> - 문서의 잡다한 정보
<body> - 화면에 표시되는 내용
<h1> - 기본적인 태그
<div> - 문서의 구역을 나누는 태그
<p> - 문서의 문단을 나누는 태그
<a href=""> - 외부 링크를 참조할 수 있는 태그
<input type> - 입력을 받을 수 있는 태그
<button> - 버튼을 넣을 수 있는 태그
<ul><li> - 목록과 리스트를 담을 수 있는 태그
```
```
<!DOCTYPE html>
<html>
    <head>
        <!-- 문서의 잡다한 정보 -->
         <title>스타트핏: 운동의 시작</title>
    </head>
    <body>
        <!-- 화면에 표시되는 내용 -->
        <h1>스타트핏: 운동의 시작</h1>

        <div>
            <h1>기초 체력업! 무분할 루틴</h1>
            <p>운동을 처음 시작하는 헬린이 모여</p>
            <a href="http://www.naver.com">지금 시작하기</a>
        </div>

        <div>
            <h1>초보탈출! 3분할 루틴</h1>
            <p>운동 좀 했니? 드루와</p>
            <a href="http://www.naver.com">지금 시작하기</a>
        </div>

        <div>
            <h1>나만의 운동 목표 설정</h1>
            <input type="text" placeholder="목표입력">
            <button onclick="alert('레츠기릿!')">저장하기</button>
            <ul>
                <li><a href="#">웨이트로 몸짱되기!</a></li>
                <li><a href="#">유산소로 다이어트!</a></li>
                <li><a href="#">필라테스로 유연성과 코어잡기</a></li>
            </ul>
        </div>
    </body>
</html>
```

## CSS 선택자
CSS 기본 문법
```
(선택자)(선언시작)(속성명):(속성값);(선언종료)
h1{color:red;}
- 페이지 안에 있는 모든 h1태그에 대해서 글자색깔을 빨강으로 바꿔라
```
**선택자(selector)** - 웹페이지에서 원하는 태그를 선택하는 문법   
클래스 선택자 - 클래서(태그에 별명을 주는 것) 속성 값으로 선택하는 것   
```
.(클래스명)(선언시작)(속성명):(속성값);(선언종료)
#(ID명)(선언시작)(속성명):(속성값);(선언종료)
(부모태그)>(자식태그)(선언시작)(속성명):(속성값);(선언종료)
```
```
<!DOCTYPE html>
<html>
    <head>
        <!-- 문서의 잡다한 정보 -->
         <title>스타트핏: 운동의 시작</title>
         <style>
            #main-title {color: orange;}
            .sub-title{font-size: 24px;}
            .box{background-color: steelblue; padding: 15px; margin-bottom: 20px; border-radius: 5px;}
            .box > a{color: white;}
            .box > p{color: lightskyblue}
         </style>
    </head>
    <body>
        <!-- 화면에 표시되는 내용 -->
        <h1 id="main-title">스타트핏: 운동의 시작</h1>

        <div class="box">
            <h1 class="sub-title">기초 체력업! 무분할 루틴</h1>
            <p>운동을 처음 시작하는 헬린이 모여</p>
            <a href="http://www.naver.com">지금 시작하기</a>
        </div>

        <div class="box">
            <h1 class="sub-title">초보탈출! 3분할 루틴</h1>
            <p>운동 좀 했니? 드루와</p>
            <a href="http://www.naver.com">지금 시작하기</a>
        </div>

        <div class="box">
            <h1 class="sub-title">나만의 운동 목표 설정</h1>
            <input type="text" placeholder="목표입력">
            <button onclick="alert('레츠기릿!')">저장하기</button>
            <ul>
                <li><a href="#">웨이트로 몸짱되기!</a></li>
                <li><a href="#">유산소로 다이어트!</a></li>
                <li><a href="#">필라테스로 유연성과 코어잡기</a></li>
            </ul>
        </div>
    </body>
</html>
```

## requests, Beautifulsoup4 사용법 빠르게 알아보기
**정적(static) 페이지** - 데이터의 추가적인 변경이 일어나지 않는 페이지(응답받은 HTML에 원하는 정보가 들어있음)   
데이터 받아오기   
1. 파이썬에서 서버에 요청을 보내고 응답받기
2. HTTP통신으로 HTML 받아오기 - requests 라이브러리 사용

데이터 뽑아내기   
1. HTML에서 원하는 부분만 추출
2. CSS 선택자를 잘 만드는 것이 핵심 - Beautifulsoup4 라이브러리 사용

```
import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding.pythonanywhere.com/basic")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
soup.select_one(".brand-name")
soup.select_one(".brand-name").text
soup.select_one(".brand-name").attrs
soup.select_one(".brand-name").attrs['href']
```

## 실전 크롤링 1단계: 한 개의 상품 크롤링 하는 법
```
import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding.pythonanywhere.com/basic")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
category = soup.select_one(".product-category").text
name = soup.select_one(".product-name").text
link = soup.select_one(".product-name > a").attrs['href']
price = soup.select_one(".product-price").text.strip().replace(',','').replace('원','')

print(category, name, link, price)
```

## 실전 크롤링 2단계: 여러 개의 상품 크롤링 하는 법 [포레스트 이론]
숲 - 페이지 전체 HTML   
나무 - 원하는 정보를 모두 담는 태그   
1. 숲에서 원하는 정보를 모두 담고 있는 나무를 찾는다
2. CSS 선택자를 만들어 테스트한다
3. soup.select("CSS선택자")로 숲에서 나무들을 뽑는다
4. 반복문을 돌면서 나무에서 하나씩 열매를 추출한다

```
import requests
from bs4 import BeautifulSoup

response = requests.get("https://startcoding.pythonanywhere.com/basic")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
items = soup.select(".product")
for item in items:
    category = item.select_one(".product-category").text
    name = item.select_one(".product-name").text
    link = item.select_one(".product-name > a").attrs['href']
    price = item.select_one(".product-price").text.split('원')[0].replace(',', '')
    print(category, name, link, price)
```

## 실전 크롤링 3단계: 여러 개의 페이지 크롤링 하는 법 [URL 조작자]
**URL(Uniform Resource Locator)** - 인터넷 주소 형식
1. Protocol - Https://
2. Domain - www.naver.com/
3. Path - search.naver? 
4. Parameter - where=news&query=삼성전자 (key=value)

페이징 알고리즘
1. 페이지를 바꾸면서 URL이 변경되는 부분을 찾는다
2. 페이지를 증가시키면서 요청을 보낸다

```
import requests
from bs4 import BeautifulSoup

for i in range(1,5):
    response = requests.get(f"https://startcoding.pythonanywhere.com/basic?page={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select(".product")
    for item in items:
        category = item.select_one(".product-category").text
        name = item.select_one(".product-name").text
        link = item.select_one(".product-name > a").attrs['href']
        price = item.select_one(".product-price").text.split('원')[0].replace(',', '')
        print(category, name, link, price)
```

## 실전 크롤링 4단계: 크롤링한 데이터 엑셀에 저장하는 법
pandas - 데이터분석 라이브러리   
openpyxl - 엑셀 자동화 라이브러리   

1. 비어있는 리스트를 만들고 데이터를 한행씩 추가한다
2. 데이터 프레임을 만들고 엑셀에 저장한다
```
import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
for i in range(1,5):
    response = requests.get(f"https://startcoding.pythonanywhere.com/basic?page={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select(".product")
    for item in items:
        category = item.select_one(".product-category").text
        name = item.select_one(".product-name").text
        link = item.select_one(".product-name > a").attrs['href']
        price = item.select_one(".product-price").text.split('원')[0].replace(',', '')
        print(category, name, link, price)
        data.append([category, name, link, price])

# 데이터 프레임 만들기
df = pd.DataFrame(data, columns=['카테고리', '상품명', '상세페이지링크', '가격'])
df
# 엑셀 저장
df.to_excel('result.xlsx', index=False)
```