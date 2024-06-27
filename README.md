# 텍스트 분석 대시보드 

## 개요 
- PyQT를 활용해 한국어 텍스트 분석을 용이하게 만든 스탠드얼론 앱입니다. 
- 

## 실행 방법 

### 1. 파이썬 가상환경 설치하기 

```sh
python -m venv
```
### 2. 가상환경 활성화 하기 

- Window의 경우 
`Scripts\activate.ps1`

- Mac의 경우 
`source Scripts/bin/activate`


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
    - read_df : xlsx, xls, csv, parquet 등 다양한 형식의 파일 읽어 드

### 메인 

분석할 텍스트 파일을 입력하고 간단하게 확인할 수 있는 페이지 입니다. 

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