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
chat_completion= client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are blog writing assistant. If user sends some content, Extract 5 keywords and pick user's expression."
        },
        {
            "role": "user",
            "content": 
            '''
            blog data 
            '''
        },
        
    ], 
    model = model
)

print(chat_completion)