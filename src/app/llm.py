# src/app/llm.py
from google import genai
from google.genai.types import HttpOptions # 🔥 이거 추가
from configs.config import settings

class GeminiLLM:
    def __init__(self):
        # api_version은 http_options 안에 넣어야 합니다.
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
            http_options=HttpOptions(api_version="v1") # 🔥 수정됨
        )

    def generate(self, prompt: str) -> str:
        # 아까 리스트에서 확인하신 모델명을 넣어주세요. (예: gemini-2.0-flash 등)
        # 만약 gemini-3.0-pro가 목록에 없으면 404가 날 수 있으니 확인 필수!
        res = self.client.models.generate_content(
            model="models/gemini-2.5-flash", 
            contents=prompt
        )
        return res.text