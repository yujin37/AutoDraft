import requests
from openai import OpenAI
import json

with open('config.json', 'r') as config_file:
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
# 사용자 입력 (샘플 데이터)
user_input = """
This blog focuses on the best practices for web development in 2024. 
We cover essential topics like performance optimization, accessibility, 
and the latest trends in JavaScript frameworks.
"""

# Chat Completion 요청
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": (
                "You are a text analysis assistant. "
                "Analyze the user's input, extract 5 key topics, and describe the writing style. "
                "Focus on tone, word choice, and structure."
            ),
        },
        {"role": "user", "content": user_input},
    ],
    model=model,
)

# 출력 결과
print("Response:")
print(response)