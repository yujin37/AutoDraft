from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import token_model

# T5 모델과 T5 토크나이저 로드
model_name = "t5-small"  # 예시로 작은 T5 모델 사용, 필요에 따라 변경 가능
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# 사용자 입력 텍스트 (예시)
user_input = """
백준 문제 풀이를 하다가 새로운 개념이 있어서 문제 풀이와 함께 정리해보려고 한다.
문제 정보는 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
"""

# 텍스트를 "extract keywords:"로 분석하기
input_text = "extract keywords: " + user_input  # 'extract keywords:'라는 프롬프트 추가

# 토크나이징
encoded_inputs = token_model.tokenizer_model(input_text) 

# 모델에 입력하고 출력 얻기
with torch.no_grad():
    output = model.generate(encoded_inputs['input_ids'], max_length=200)

# 출력 텍스트 디코딩
decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
print(decoded_output)
