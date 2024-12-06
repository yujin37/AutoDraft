from transformers import T5Tokenizer
tokenizer = T5Tokenizer(vocab_file="./setence_token_model/t5-sp-bpe-nsmc-byte-fallback.model")
tokenizer.save_pretrained("./setence_token_model/t5-tokenizer-bpe-nsmc-byte-fallback")
def tokenizer_model(lines):
  #lines = [ # 이 부분은 추후 자동으로 가져오도록 처리할 예정
  #  "백준 문제 풀이를 하다가 새로운 개념이 있어서 문제 풀이와 함께 정리해보려고 한다.",
  #  "문제 정보",
  #  "문제",
  #  "골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.",
  #  "짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다.",
  #  "짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자.",
  #  "두 소수의 순서만 다른 것은 같은 파티션이다.",
  #  ]
  print(lines)
  encoded_inputs = tokenizer(lines, padding=True, truncation=True, return_tensors="pt", max_length=512)
  return encoded_inputs

#for i in range(len(lines)):
#  decoded_sequence = tokenizer.decode(encoded_inputs['input_ids'][i], skip_special_tokens=True)
#  #print(lines[i])
#  print(decoded_sequence)