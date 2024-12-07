from openai import OpenAI
import json
import firebase_admin
from firebase_admin import credentials, firestore

#llama 모델 관련 설정
with open('../config.json', 'r') as config_file:
    config = json.load(config_file)
    SECRET_KEY = config.get('LAMBDA_KEY')

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY가 설정되지 않았습니다.")

# Lambda Labs API 키와 베이스 URL 설정
api_key = SECRET_KEY  # Lambda Labs API Key
api_base_url = "https://api.lambdalabs.com/v1"
model = "llama3.1-70b-instruct-berkeley"

client = OpenAI(
    api_key=api_key,
    base_url=api_base_url,
)

#사용자 데이터 가져오기.
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 사용자 입력 텍스트
user_input = """
백준 문제 풀이를 하다가 새로운 개념이 있어서 문제 풀이와 함께 정리해보려고 한다.
문제 정보는 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
"""
try:
    docs = db.collection("blogdata").get()
    for doc in docs:
        user_input = doc.to_dict().values()
        user_input = ''.join(map(str, user_input))
        #print(user_input)
        # Chat Completion 요청
        
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a text analysis assistant. "
                        "Analyze the user's input, describe the writing style. "
                        "This text is markdown type"
                        "Focus on tone, word choice, and structure. Say Simple"
                    ),
                },
                {"role": "user", "content": user_input},
            ],
            model=model,
        )
except Exception as e:
    print(f'오류 밠생: {e}')
# 출력 결과
print("Response:")
print(response)