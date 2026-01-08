# src/rag/retriever.py
import faiss
import numpy as np
from google import genai
from configs.config import settings


class RAGRetriever:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.texts = []
        self.index = None

    def _embed(self, text: str) -> np.ndarray:
        res = self.client.models.embed_content(
            model="text-embedding-004",
            contents=text
        )
        return np.array(res.embeddings[0].values, dtype="float32")

    def build(self, docs: list[str]):
        self.texts = docs
        vectors = np.vstack([self._embed(d) for d in docs])
        self.index = faiss.IndexFlatL2(vectors.shape[1])
        self.index.add(vectors)

    def search(self, query: str, k: int = 2):
        vec = self._embed(query).reshape(1, -1)
        _, idx = self.index.search(vec, k)
        return [self.texts[i] for i in idx[0]]
