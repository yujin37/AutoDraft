from openai import OpenAI
import json
import firebase_admin
from firebase_admin import credentials, firestore
import re

with open('../config.json', 'r') as config_file:
    config = json.load(config_file)
    SECRET_KEY = config.get('OPENAI_KEY')

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY가 설정되지 않았습니다.")

client = OpenAI(api_key=SECRET_KEY)

#사용자 데이터 가져오기.
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 사용자 입력 텍스트
user_input = """
백준 문제 풀이를 하다가 새로운 개념이 있어서 문제 풀이와 함께 정리해보려고 한다.
문제 정보는 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
"""

def new_style(input_text: str) -> str:
    # 새로운 사용자 텍스트를 입력 받음.  이건 자유롭게 사용할 수 있도록
    try:
        # OpenAI를 사용하여 텍스트 분석
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a text analysis assistant. Analyze the text and suggest an appropriate style type. "
                        "The available style types are: event_recap, informative, analysis, problem_solving, tutorial, developer_experience, "
                        "tech trends, tech comparison, project update, and development philosophy. "
                        "Please provide the chosen style type and its characteristics."
                    ),
                },
                {"role": "user", "content": input_text},
            ],
            temperature=0,
        )
        style_features = response.choices[0].message.content
        style_type_match = re.search(r'"([^"]+)"', style_features)
        if style_type_match:
            style_type = style_type_match.group(1).strip().lower()
        # 파싱 결과를 딕셔너리로 반환
        return {"style_type": style_type or "neutral", "features": style_features or {}}
    except Exception as e:
        print(f"Error in new_style function: {e}")
        return {}
    
# 기존에 저장된 정보를 바탕으로 분석 진행
def style_function(input_text: str) -> str:
    try:
        # 새로운 텍스트의 스타일 분석 및 타입 결정
        style_info = new_style(input_text)
        style_type = style_info.get('style_type', '').strip()
        if style_type.endswith('.'):
            style_type = style_type[:-1]  # 점을 제거

        # 특징 추출: 'features'에서 텍스트 추출
        features = style_info.get('features', '').strip()
        # Firestore에서 데이터 가져오기
        docs = db.collection("user_feature").get()
        for doc in docs:
            user_data = doc.to_dict()
            
            # 해당 스타일 종류의 기존 텍스트 가져오기
            existing_style_text = user_data.get(style_type, "")
            
            # 새로운 텍스트의 특징 분석 (new_style 호출)
            #style_features = new_style(input_text)
            
            # 새로운 텍스트 생성 로직
            updated_text = generate_updated_text(existing_style_text, features)
            
            # Firestore에 수정된 데이터 저장
            doc_ref = db.collection("user_feature").document(doc.id)
            doc_ref.update({style_type: updated_text})
            print(f"Updated text for style '{style_type}':\n{updated_text}")
            
            return updated_text
        
    except Exception as e:
        print(f"오류 발생: {e}")
        return ""
def generate_updated_text(existing_text: str, style_features: dict) -> str:
    """
    새로운 텍스트와 기존 텍스트를 스타일 특징에 맞게 조합하여 생성.
    """
    try:
        # OpenAI를 사용하여 새로운 텍스트 생성
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a text generator. Combine the new input text with the existing text, "
                        #"while blending both the existing and new style features into the output."
                        "Please define your style by looking at existing and new styles."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Existing style text: {existing_text}\n"
                        f"New Style features: {style_features}"
                    ),
                },
            ],
            temperature=0
        )
        updated_text = response.choices[0].message.content
        return updated_text
    except Exception as e:
        print(f"Error in generate_updated_text function: {e}")
        return f"{existing_text}"