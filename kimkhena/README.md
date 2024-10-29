# 웹 크롤링 기초
**웹크롤링**(Web Crawling) - Web(거미줄) + Crawling(기어다니다) 웹상의 정보들을 탐색하고 수집하는 작업

웹크롤링의 활용
- 데이터 분석 과정
- 웹사이트 자동화
- 인공지능의 학습 데이터

HTTP 통신을 통해 웹 브라우저와 웹서버 사이에 데이터를 주고 받는다. HTTP를 통해 데이터를 긁어온다.

## 웹개발의 3가지 요소
- HTML : 구조
- CSS : 디자인
- JavaScript : 동작

### HTML
> <태그이름 속성="속성값"'> 내용 </태그이름>

태그 - HTML문서의 모양과 행동양식을 정해주는 명령어 이름

속성(attribute) : 태그의 추가적인 정보(속성은 여러 개 부여할 수 있다, 속성은 없어도 된다)


### CSS
>선택자 {속성명:속성값}

선택자 - 웹페이지에 원하는 태그를 선택하는 문법


```
<body>
<h1>Pick This</hl>
<p>Pick This, Too</p>
</body>/
```
태그 선택자 - 태그 이름으로 선택하는 것


```
. large {
font-size : 50px;
font-weight : 600;
}

<body>
<p>Do not pick this</p>
<p class="large" >Pick this</p>
<p class="large"| >Pick this</p>
</body>
```

클래스 선택자 - 클래스 속성 값으로 선택하는 것 (같은 유형으로 반복되는 태그들을 유형별로 분류하고 싶을 때 씁니다.)

```
#title {
font-size : 32px;
text-decoration : underline;
}

<body>
<p id="title">Pick this</p>
<p>Do not pick this</p>
<p>Do not pick this</p>
</body>
```

아이디 선택자 -아이디 속성 값으로 선택하는 것


```
<body>
  <div class="header">
    <p>Pick This</p>
    <p>Pick This</p>
  </div>
  <div class="section">
    <p>Do not Pick This</p>
    <p>Do not Pick This</p>
  </div>
</body>

.header > p {font-size: 30px;}
```

자식 선택자 - 바로 아래 자식태그를 선택하는 것


## 정적 페이지 크롤링

**정적 페이지** - 데이터의 추가적 변경이 일어나지 않는 페이지

데이터 받아오기: 파이썬에서 서버에 요청을 보내고 응답받기

데이터 뽑아내기: HTML에서 원하는 부분만 색출 (BeatifulSoup4)

requests, bs4 install


```
import requests
#웹사이트 불러오기
response = requests.get("https://www.yanolja.com/reviews/domestic/1000108384")
#웹이 잘 불러나왔는지 확인 (200)
response.status_code

# html 텍스트
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#태그 추출
soup.select_one(".class")

#태그 내 텍스트 추출
soup.select_one(".class").text

#태그 내 주소 추출 
soup.select_one(".class").attrs[href]

#공백제거
soup.select_one(".class").strip()



# 태그 전쳬를 리스트로 반환 
items = soup.select(".class")


각 상위 태그내의 하위 타그 찾기
for item in items:
    category = item.select_one("product-category").text
    name = item.select_one(".product-name").text
    link = item.select_one(".product-name > a").attrs['href']
    price = item.select_one(".product-price").text.split('원')[0].replace(',',)
    print(category, name, link, price)
I
```
### 여러개의 페이지 크롤링 하는 법: url 구조를 분석하고 파라미터의 구조를 파악 후 바꿔서 원하는 페이지를 찾으면 된다.

```
import requests
from bs4 import BeautifulSoup

for i in range(1, 5):
response = requests.get(f"https://startcoding.pythonanywhere.com/basic?page={i}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
items = soup.select(".product")
for item in items:
category = item.select_one(".product-category").text
print(category)
```

### 크롤링한 데이터 엑셀에 저장하는 방법

openpyxl, pandas 다운로드 필요

1. 비어있는 리스트를 만들고 데이터를 한 행 씩 추가한다.
2. 데이터 프레임으로 만들고 엑셀로 저장한다

```
import pandas as pd
data = []

data.append([category, name])
# 데이터 프레임 란들기
df = pd.DataFrame(data, columns=['카테고리, 상품명'])
# 엑셀 저장, 인덱스를 없애줌
df.to_excel('result.xlsx', index=Falfe)
```