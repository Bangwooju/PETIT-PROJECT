import csv
import re
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from rag.retriever import RAGRetriever
from app.llm import GeminiLLM
from mcp.tuner import MCP

app = FastAPI()
templates = Jinja2Templates(directory="src/app/templates")

# 초기화
retriever = RAGRetriever()
llm = GeminiLLM()
mcp = MCP()

# CSV 파일 경로
CSV_PATH = Path("queries.csv")
if not CSV_PATH.exists():
    CSV_PATH.write_text("query,result\n", encoding="utf-8")  # 헤더 추가

# 예시 문서로 RAG 빌드
docs = [
    "Avoid SELECT *. Always specify required columns.",
    "Use indexes on frequently filtered columns.",
    "Avoid subqueries when JOIN can be used.",
    "Use LIMIT when querying large tables.",
    "Prefer EXISTS over IN for large subqueries."
]
retriever.build(docs)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
def tune_sql(request: Request, sql: str = Form(...)):
    # RAG 검색
    rag_contexts = retriever.search(sql, k=2)

    # MCP 정책
    mcp_rules = mcp.policy(sql)

    # LLM 프롬프트
    prompt = f"""
너는 데이터베이스 성능 튜닝 전문가다.

[입력 SQL]
{sql}

[MCP 튜닝 정책]
{mcp_rules}

[과거 튜닝 참고 사례]
{chr(10).join(rag_contexts)}

위 정보를 기반으로
- 성능이 더 좋은 SQL로 재작성하라
- 결과 의미는 동일해야 한다
- 불필요한 컬럼 조회를 제거하라

튜닝된 SQL만 출력하라.
"""
    tuned_query = llm.generate(prompt)

    # Markdown 코드 블록 제거
    cleaned_query = re.sub(r"```(?:sql)?\n(.*?)```", r"\1", tuned_query, flags=re.DOTALL).strip()

    # CSV에 기록
    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([sql, cleaned_query])

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "query": sql, "result": cleaned_query}
    )


@app.get("/history", response_class=HTMLResponse)
def history(request: Request):
    # CSV 읽기
    records = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return templates.TemplateResponse("history.html", {"request": request, "records": records})


@app.get("/download")
def download():
    return FileResponse(path=CSV_PATH, filename="queries.csv", media_type="text/csv")
