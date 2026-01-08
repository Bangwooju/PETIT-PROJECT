from google import genai
from google.genai.types import HttpOptions

# 1. 클라이언트 생성 시 api_version을 'v1'으로 고정합니다.
client = genai.Client(api_key="AIzaSyAGZm0KszgvfaVFYygRBbvBTpcEhZLCBcA")

try:
    # 1. 사용 가능한 모델 목록 가져오기
    print("--- 사용 가능한 모델 목록 확인 중 ---")
    available_models = []
    for m in client.models.list():
        # 'generateContent' 액션이 지원되는 모델만 필터링
        if 'generateContent' in m.supported_actions:
            available_models.append(m.name)
            print(f"발견된 모델: {m.name}")

    if not available_models:
        print("사용 가능한 모델을 찾지 못했습니다.")
    else:
        # 2. 리스트 중 첫 번째 모델(보통 최신 버전) 선택
        target_model = available_models[0]
        print(f"\n[{target_model}] 모델을 사용하여 질문을 던집니다...")

        # 3. 실제 질문 던지기
        response = client.models.generate_content(
            model=target_model,
            contents="오늘 날짜가 6월 11일이라고? 왜...? 다시 생각해봐 "
        )

        print("\n--- AI 응답 결과 ---")
        print(response.text)

except Exception as e:
    print(f"\n오류 발생: {e}")