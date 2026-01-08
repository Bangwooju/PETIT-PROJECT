# src/mcp/tuner.py
class MCP:
    def policy(self, query: str) -> str:
        return f"""
너는 SQL 쿼리 튜닝 전문가다.

목표:
- 불필요한 컬럼 제거
- WHERE 조건 명확화
- 가독성과 성능 개선

원본 쿼리:
{query}
"""
