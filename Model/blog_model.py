from openai import OpenAI
import json
from firebase_admin import credentials, firestore
import streamlit as st

with open('../config.json', 'r') as config_file:
    config = json.load(config_file)
    SECRET_KEY = config.get('OPENAI_KEY')

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY가 설정되지 않았습니다.")

client = OpenAI(api_key=SECRET_KEY)

cred = credentials.Certificate("../serviceAccountKey.json")
db = firestore.client()

def blog_function(input_text: str, topic: str, user: str) -> str:
    user_writing_style = ""
    doc_ref = db.collection("user_feature").document(user)
    doc = doc_ref.get()

    # 문서가 없으면 새로 생성하고, 있으면 업데이트
    if not doc.exists:
        # 문서가 없으면 새로 생성
        doc_ref.set({
            "informartive": ""
        })
        print(f"Document for user {user} created.")
    else:
        # 문서가 존재하면 업데이트 (이 경우에는 문서 수정 로직을 추가할 수 있습니다)
        print(f"Document for user {user} already exists.")
    
    # Firestore 문서 확인
    if doc.exists:
        data = doc.to_dict()  # 문서 데이터를 딕셔너리로 변환
        if topic in data:  # topic 값 존재 여부 확인
            print(f"Matching value found for topic '{topic}': {data[topic]}")
            user_writing_style = data[topic]
        else:
            print(f"No matching topic value found for '{topic}'.")
            user_writing_style = "No specific writing style found for the given topic."
    else:
        print(f"Document '{user}' does not exist.")
        user_writing_style = "No user writing style available."

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a blog writing assistant. "
                        f"The user's writing style is as follows: {user_writing_style} "
                        "When the user provides input, generate a blog-style response based on the user's writing preferences and previously stored writing style."
                    ),
                },
                {"role": "user", "content": input_text},
            ],
        )
        return response.choices[0].message.content # 생성된 블로그 글 반환
    except Exception as e:
        print(f"Error during Lambda Labs API call: {e}")
        return "Error generating blog content."