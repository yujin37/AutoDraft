from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# 모델과 토크나이저 불러오기
tokenizer = AutoTokenizer.from_pretrained("czearing/article-title-generator")
model = AutoModelForSeq2SeqLM.from_pretrained("czearing/article-title-generator")

def title_function(input_text: str) -> str :
    # 입력 텍스트 설정
    #input_text = "A groundbreaking study published in Nature reveals that scientists have discovered a way to reverse the effects of aging in mice. By targeting specific proteins in the body, researchers were able to restore the animals' muscle strength, improve cognitive functions, and extend their lifespan by 30%. This revolutionary finding has opened new possibilities for anti-aging treatments in humans. Clinical trials are expected to begin within the next five years, raising hopes for healthier and longer lives."
    #영어만 가능하고 현재 한글이 입력이 안 받아지는 현상
    #추가 데이터 학습이 가능하면 추가학습으로 개선할 계획

    # 토크나이저로 입력 텍스트 인코딩
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding=True)

    # 모델로부터 결과 생성
    output_ids = model.generate(**inputs, max_length=20, num_beams=5, early_stopping=True)

    # 결과 디코딩
    generated_title = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # 생성된 기사 제목 출력
    print("Generated Article Title:", generated_title)

    return generated_title
