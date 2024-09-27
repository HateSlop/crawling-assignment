# crawling-assignment
크롤링 과제 제출을 위한 레포지토리입니다. 

## 제출 방법

1. 자신의 깃허브 아이디로 원본 레포지토리를 Fork 해주세요.
2. Fork한 레포지토리를 Clone 해주세요.
3. 브랜치 만든 다음에 개인 폴더 만들어주세요. 
4. 작업 하시고 커밋 후 오리진으로 푸시해주시면 됩니다.
5. main 으로 풀리퀘 날려주시면 됩니다. merge 는 하시면 안돼요! 풀리퀘 제목 :?[이름] 실습 과제 제출합니다.

### 예시

```bash
git clone git@github.com:Nakedgreeen/crawling.git  # 클론
cd crawling # 프로젝트 루트로 이동
git checkout -b Minseok # 브랜치 생성 (본인의 브랜치, 폴더 등 생성)
mkdir Minseok # 개인 폴더 만들기
cd Minseok # 개인 폴더로 이동
git add . # 작업 후 add
git commit -m "[feat] ~~" # 커밋
git push origin Minseok # 오리진에 푸시
```

### 폴더구조

```bash
.
├── README.md # 프로젝트 설명 리드미 (수정X)
└── minseongh #(개인 폴더)
    └── crawling-practice.py
```

## 커밋 컨벤션

feat: 새로운 기능 추가  
fix: 버그 수정  
docs: 문서 수정  
style: 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우  
refactor: 코드 리팩토링  
test: 테스트 코드, 리팩토링 테스트 코드 추가  
chore: 빌드 업무 수정, 패키지 매니저 수정, production code와 무관한 부분들 (.gitignore, build.gradle 같은)  
comment: 주석 추가 및 변경  
remove: 파일, 폴더 삭제  
rename: 파일, 폴더명 수정
