import openai
import json
import firebase_admin
from firebase_admin import credentials, firestore

with open('../config.json', 'r') as config_file:
    config = json.load(config_file)
    SECRET_KEY = config.get('OPENAI_KEY')

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY가 설정되지 않았습니다.")

openai.api_key = SECRET_KEY

#사용자 데이터 가져오기.
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 사용자 입력 텍스트
user_input = """
백준 문제 풀이를 하다가 새로운 개념이 있어서 문제 풀이와 함께 정리해보려고 한다.
문제 정보는 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
"""
def style_function(input_text: str, style_type: str = None) -> str:
    try:
        docs = db.collection("blogdata").get()
        for doc in docs:
            user_input = doc.to_dict().values()
            user_input = ''.join(map(str, user_input))
            #print(user_input)
            # Chat Completion 요청
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a text analysis assistant. And You're programmer and developer. "
                            "Analyze the user's input and provide the following breakdown:\n"
                            "- Tone: Describe the overall tone of the text (e.g., formal, informal, neutral, etc.).\n"
                            "- Word Choice: Evaluate the words and phrases used (e.g., complex, simple, professional, casual, etc.).\n"
                            "- Structure: Provide an analysis of the structure of the text (e.g., clear, well-organized, fragmented, etc.)."
                        ),
                    },
                    {"role": "user", "content": user_input},
                ],
            )
    except Exception as e:
        print(f'오류 밠생: {e}')
    # 출력 결과
    response = response['choices'][0]['message']['content']
    print("Response:")
    print(response)

    if response:
        return "success"
    else:
        return "fail"