# 텍스트 분석 대시보드

## 개요
- PyQT를 활용해 한국어 텍스트 분석을 용이하게 만든 스탠드얼론 앱입니다.
- 민원 분석에서 자주 쓰이는 키워드 분석이나 차트를 그리기 쉽게 만들었습니다.

## 실행 방법


### 1. 파이썬 가상환경 설치하기

```sh
python -m venv
```
### 2. 가상환경 활성화 하기

- Window의 경우
`Scripts\activate.ps1`

- Mac의 경우
`source bin/activate`

### 3. 파이썬 요구 패키지 설치하기
`pip install pyinstaller pyside6 plotly pandas polars`

### 4. main.py 실행하기
`python \src\main.py`

### 5. 실행 파일 만들기
`pyinstaller src/win.py -n "test_app" --noconsole --onefile`

## 구성

- 페이지
    - [메인](#메인)
    - [탐색적 분석](#탐색적-분석)
    - [텍스트 마이닝](#텍스트-마이닝)
    - 사전
    - AI
- 변수
    - df : dataframe
    - df.cols : [일자, 분류, 내용]
- 컴포넌트
    - read_df : xlsx, xls, csv, parquet 등 테이블 형식의 읽어서 데이터테이블로 표현
    - filter_df(time_config, ) :
    - export_df : xlsx 파일로 출력하기
    - tf_df : term-frequency로 변형하기 (if df.tf_df ? ) -> 있으면 하고 없으면 만들기
    - to_wordcloud(df, config)
    - to_network(df, config)

### 메인

분석할 텍스트 파일을 입력하고 간단하게 확인할 수 있는 페이지 입니다.
- component : 파일 입력 드래그앤 드랍 
    - 드래그 했을때 
    - 클릭 했을 때 

### 탐색적 분석

- 분포
- 시계열 차트

### 텍스트 마이닝

### 사전

자연어 분석 시 참조할 사용자 단어, 불용어, 오탈자 수정을 정의할 수 있습니다. \
- *사용자 단어* : 합성어 등 일반 단어 사전에는 없으나, 분석할 텍스트에 빈번하게 등장하는 경우
- 불용어 : 자연어 분석에 불필요한 조사나 특정 단어를 정의할 수 있습니다. (날짜, 숫자, 영어, 특수문자 등 옵션 )
- 오탈자 수정 :


## 컴포넌트 구성

### 메뉴바
- 파일
- 자바스크립트 리소스 불러오기
- 문의 페이지
- 재설치 하기 링크

### 파일 입출력

### 텍스트 분석


## Todo

#### 메뉴바에 추가할 것
- 쉘 실행하는 방법?
    - 최초 설정 : js 설치하는 코드, 폰트 같은것
    - Ollama AI 모델 설치하는 파워쉘 코드
    - user/document/밑에 필요한 js파일 가져다 놓기
