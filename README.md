# 텍스트 분석 대시보드

## 개요
- PyQT를 활용해 한국어 텍스트 분석을 용이하게 만든 스탠드얼론 앱입니다.
- 민원 분석에서 자주 쓰이는 키워드 분석이나 차트를 그리기 쉽게 만들었습니다.

## 실행 방법

### 0. 업무망에서 실행하는 방법 
- [link to excloud]() 에서 파워쉘 코드를 다운로드후 실행

### 1. 파이썬 가상환경 설치하기

```sh
python -m venv
```
### 2. 가상환경 활성화 하기

- Window의 경우
```sh
Scripts\activate.ps1
```
- Mac의 경우
```sh
source bin/activate
```

### 3. 파이썬 요구 패키지 설치하기
```sh
pip install pyside6 plotly pandas
```

### 4. main.py 실행하기
```sh
python \src\main.py
```

### 5. 실행 파일 만들기

- pyinstaller 
```sh
pyinstaller src/win.py -n "test_app" --noconsole --onefile --exclude PyQt5 --icon=src/public/icon.ico

pyinstaller test_app.spec
pyinstaller TextD.spec --noconfirm
```

### 6. ui 파일 빌드하기 
```sh
pyside6-designer
pyside6-uic src/ui/FileInput.ui -o src/ui/FileInput.py
pyside6-uic src/ui/TextMining.ui -o src/ui/TextMining.py 
pyside6-uic src/ui/Plot.ui -o src/ui/Plot.py
pyside6-uic src/ui/Dictionary.ui -o src/ui/Dictionary.py
```

## 구성

- 페이지
    - [메인](#메인)
    - [탐색적 분석](#탐색적-분석)
    - [텍스트 마이닝](#텍스트-마이닝)
    - [AI]
    - [사전]
    - [메뉴얼]
- 변수 main.data
    - df : dataframe
    - df.cols : [일자, 분류, 내용]
- 컴포넌트
    - read_df : xlsx, xls, csv, parquet 등 테이블 형식의 읽어서 데이터테이블로 표현
    - filter_df(time_config, ) :
    - export_df : xlsx 파일로 출력하기
    - tf_df : term-frequency로 변형하기 (if df.tf_df ? ) -> 있으면 하고 없으면 만들기
    - to_wordcloud(df, config)
    - to_network(df, config)


### 📃 페이지 

#### 메인 탭 

> 분석할 텍스트 파일을 입력하고 간단하게 확인할 수 있는 페이지 입니다.

- 위젯 
    - 파일 입력 : 분석할 민우너 파일 입력
        -> 만약 엑셀 위에 첫 행부터 시작 안할 경우를 고려,
        -> 입력 받으면 자동으로 열 세팅 실행 
    - 열 선택 : 입력 받으면 일단 자동으로 분석열을 선택하나, 수동으로도 선택할 수 있도록 라벨, 없음도 옵션으로 하기  
    - 간단한 정보 표출 : 파일명, 행 개수, 등
        - 일자열 지정되면 : 기간 범위 
        - 카테고리열 지정되면 : 각각의 건수 
        - 텍스트열 : 중복건수, 빈/적은 것 등 
    - 테이블 : 받은 데이터프레임 raw 정보 표출, 많으면 헤더와 테일만 표출 <- 여기서는 그냥 간단하게 파일 확인 할 수 있도록 

#### 탐색적 분석 탭 

> 라인, 바, 등 간단한 통계적 차트를 쉽게 생성할 수 있는 것

- `만약 차트 표출이 되지 않는다면, 메뉴바 -> js 설치 버튼을 누르세요.`
    - 나중에 js파일을 여러개 해서 테마를 만들수도 ?
- 공통 위젯 
    - 사이트 탭 : 
    - 필터 : 
        - 일자 : 
            - 시계열 차트면 기간 범위 선택  
        - 카테고리 : 
        - 텍스트 : 포함될 단어, 제외할 단어, 
- 개별 위젯 
    - 차트 설정 
    - 차트 뷰 
- 차트 종류 
    - 시계열 차트 : 라인, 바, 그룹
    - 분포 : 파이, 선버스트, 
    - 통계 : 그냥 표 출력하는 것 

#### 텍스트 마이닝

> 빈도 사전, 워드클라우드, 네트워크 

- 빈도 사전 : tableview 
- 워드클라우드 : plotview 
- 네트워크 : webview

#### 사전

> 텍스트 분석에서 활용한 것

자연어 분석 시 참조할 사용자 단어, 불용어, 오탈자 수정을 정의할 수 있습니다. \
- *사용자 단어* : 합성어 등 일반 단어 사전에는 없으나, 분석할 텍스트에 빈번하게 등장하는 경우
- 불용어 : 자연어 분석에 불필요한 조사나 특정 단어를 정의할 수 있습니다. (날짜, 숫자, 영어, 특수문자 등 옵션 )
- 오탈자 수정 : 

#### 설정 앤 매뉴얼 

> 매뉴얼과 각종 설명 또는 에러 발생 시 지침 

- js 재설치 
- 링크 등등 
- 폰트 위치 설정 
- 기본 열이름 설정 
- 테마 설정 
- 차트 다운로드 위치 등등 

## 컴포넌트 구성

### 메뉴바
- 파일
- 자바스크립트 리소스 불러오기
- 문의 페이지
- 재설치 하기 링크

### 파일 입출력

### 텍스트 분석

## Todo

### 메뉴바에 추가할 것

- 쉘 실행하는 방법?
    - 최초 설정 : js 설치하는 코드, 폰트 같은것
    - Ollama AI 모델 설치하는 파워쉘 코드
    - user/document/밑에 필요한 js파일 가져다 놓기
- 설정 ini 파일을 만들기 
    - 목표 : 만들어서 앱 일관성 유지 
    - setting.ini 파일 확인해서 없으면 기본 ini 파일 하나 만들기 
    - 앱 실행 최초에 ini 파일 읽어와서 환경(글로벌 변수) 구성하기 
    - 설정 페이지에서 설정을 저장하면 setting.ini 파일에 변경사항 저장하기 

---
- 상태바 
    - 현재 fdf의 열개수 : 필터링 되었는지 
    - 마지막 실행한 명령 표시해서 진행상태 알려주기 
- 메인 
    - 사이드바 
        - 파일 입력 
        - 분석 설정하기 
    - 메인 
- 텍스트마이닝 
    - 사이드바
        - 
    - 메인 
        - 단어빈도표
        - 워드클라우드
        - 네트워크
- 탐색적분석 
    - 사이드바 
    - 메인 
- AI 
    - 사이드바 
        - Ollama 연동 : 포트 
    - 메인
        - AI 분석 
- 사전 
    - 오탈자 
    - (global)불용어 
- 설정 
    - 사이드바 
        - 차트 옵션 : 기본 크기, 저장경로 등
        - ollama 옵션 : 기본 프롬프트 
        - 단어사전
    - 메인 

### 내용 
