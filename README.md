# MINI PROJECT
# MCP + RAG 기반 SQL 튜닝 웹 어플리케이션

> 이 프로젝트는 **MCP(Minimum Change Policy) + RAG(Retrieval-Augmented Generation) + LLM(Google Gemini API)**를 결합하여 SQL 쿼리를 자동으로 튜닝하고, 웹에서 결과를 확인할 수 있는 실무용 도구입니다.

---

## 👥 개발인원
방우주, chat-GPT 무료 (로그인 안함)
special thanks to 지현언니

## ⏰ 개발기간
2026-01-07 ~ 2026-01-08

## 🚀 주요 기능

- **SQL 쿼리 입력**: 웹 UI에서 SQL 쿼리를 입력할 수 있습니다.  
- **MCP 정책 적용**: SQL 최적화 규칙을 자동으로 적용합니다.  
- **RAG 검색**: 과거 SQL 튜닝 사례를 기반으로 참고 정보를 제공합니다.  
- **LLM 튜닝**: Google Gemini API를 활용해 성능 최적화 SQL 생성  
- **쿼리 기록**: 입력한 쿼리와 튜닝 결과를 CSV로 저장, 다운로드 가능  
- **웹 UI**: FastAPI + Jinja2 기반, 입력/결과/히스토리 페이지 제공  

---

## 🛠 기술 스택

- **Backend / Core Logic:** Python 3.11+, FastAPI, LangChain, FAISS, MCP, Gemini API  
- **Frontend / UI:** Jinja2, HTML, CSS  
- **Database / Storage:** PostgreSQL(로컬, RAG 학습용), CSV(쿼리 기록)  
- **Environment / DevOps:** Python Virtual Environment (`.venv`), dotenv (`.env`)  
- **Others:** python-multipart (FastAPI Form 데이터 처리)  

## 주의
현 시점 무료 AI 모델을 사용하였습니다.
실행시점 사용가능 모델 확인이 필요한 경우 루트 디렉토리의 test.py 실행하여 사용가능 모델 확인하고
llm.py 파일의 model 을 변경해주시면 됩니다.

---

## 📂 디렉토리 구조

project/
├─ .env                        # Gemini API Key 저장
├─ queries.csv                  # 쿼리 기록 CSV (자동 생성)
├─ src/
│  ├─ app/
│  │  ├─ main.py               # FastAPI 웹서버 + 튜닝 + 기록 + 다운로드
│  │  ├─ llm.py                # Gemini LLM 래퍼
│  │  └─ templates/
│  │     ├─ index.html          # SQL 입력 + 결과 화면
│  │     └─ history.html        # 쿼리 기록 확인 + 다운로드
│  ├─ rag/
│  │  └─ retriever.py           # RAG + FAISS Retriever
│  └─ mcp/
│     └─ tuner.py               # MCP 쿼리 튜닝 정책
└─ .venv/                       # 가상환경

---

## 설치 및 실행

1. 프로젝트 클론 후 가상환경 생성 및 활성화
```
git clone <your-repo-url>
cd project
python -m venv .venv

Windows
.venv\Scripts\activate

macOS / Linux
source .venv/bin/activate
```

2. 패키지 설치
```
pip install -r requirements.txt
```

3. `.env` 파일 생성 후 Gemini API Key 설정
```
GEMINI_API_KEY=your_api_key_here
```

4. 웹 서버 실행
```
uvicorn src.app.main:app --reload
```

5. 브라우저에서 접속
http://127.0.0.1:8000

---

## 웹 UI 설명

### 1. 메인 페이지 (`/`)
- SQL 입력란에 튜닝하고 싶은 쿼리 입력
- `Submit` 버튼 클릭
- 아래 영역에서 튜닝된 SQL 결과 확인

### 2. 히스토리 페이지 (`/history`)
- 과거에 입력한 쿼리와 튜닝 결과 확인 가능
- `Download CSV` 버튼으로 쿼리 기록 다운로드 가능

---

## 사용 예시

**입력 SQL**
SELECT * FROM users WHERE age > 30;

markdown
코드 복사

**튜닝 결과**
SELECT id, name, age FROM users WHERE age > 30;

> MCP 정책과 RAG 검색으로 불필요한 컬럼 제거, 성능 최적화 SQL 자동 생성

---

## 주의사항

- Gemini API Key가 필요하며 `.env` 파일에 반드시 설정해야 합니다.
- PostgreSQL은 RAG 학습 예시용이며, 필수는 아닙니다.
- CSV 쿼리 기록은 실행 시 자동 생성됩니다.

---

## 추가 정보

- FASTAPI: https://fastapi.tiangolo.com/
- LangChain: https://www.langchain.com/
- Gemini API: Google Generative AI https://developers.generativeai.google

---

## 다운로드 및 실행

1. GitHub에서 클론
2. `.env`에 API Key 설정
3. `uvicorn src.app.main:app --reload` 실행
4. 브라우저에서 `http://127.0.0.1:8000` 접속
5. SQL 입력, 결과 확인, 히스토리 다운로드 가능




*안녕하세요*
