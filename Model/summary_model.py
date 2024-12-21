import torch
import nltk
nltk.download('punkt_tab')
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM

#tokenizer = AutoTokenizer.from_pretrained("lemon-mint/gemma-ko-7b-it-v0.30")
#model = AutoModelForCausalLM.from_pretrained("lemon-mint/gemma-ko-7b-it-v0.30")
model = AutoModelForSeq2SeqLM.from_pretrained('eenzeenee/t5-base-korean-summarization')
tokenizer = AutoTokenizer.from_pretrained('eenzeenee/t5-base-korean-summarization')

prefix = "summarize: "

def summary_function(input_text: str) -> str :
    #print(input_text)
    inputs = [prefix + input_text]

    inputs = tokenizer(inputs, max_length=512, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=3, do_sample=True, min_length=10, max_length=64)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    result = nltk.sent_tokenize(decoded_output.strip())[0]
    #inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    #with torch.no_grad():  # No gradient calculation needed for inference
    #    output = model.generate(
    #        **inputs,
    #        max_length=100,         # 출력 최대 길이
    #        temperature=0.7,        # 생성 다양성을 조절하는 파라미터 (낮을수록 보수적)
    #        top_p=0.95,             # nucleus sampling 비율
    #        pad_token_id=tokenizer.eos_token_id  # 패딩 시 EOS 토큰 사용
    #    )

    # 생성된 텍스트 디코딩
    #result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result
