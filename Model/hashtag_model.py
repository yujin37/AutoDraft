import nltk
from nltk.corpus import stopwords
import re
from gensim import corpora
from gensim.models import LdaModel

# nltk 리소스 다운로드

nltk.download('stopwords')

'''
with open('../config.json', 'r') as config_file:
    config = json.load(config_file)
    ACCESS_TOKEN = config.get('INSTA_ACCESS')
    USER_ID = config.get("INSTA_ID")

ACCESS_TOKEN = ACCESS_TOKEN
USER_ID = USER_ID  # 비즈니스 계정의 사용자 ID
HASHTAG_NAME = "coffee"
'''
def preprocess_text(text):
    # 텍스트 전처리: 소문자화, 정규 표현식으로 알파벳만 추출, 불용어 제거
    stop_words = set(stopwords.words('english'))
    # 소문자화 및 정규 표현식으로 단어 추출
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    # 불용어 제거
    filtered_tokens = [word for word in words if word not in stop_words]
    return filtered_tokens

def topic_modeling(input_text, num_topics=1, passes=10):
    # 텍스트 전처리
    processed_texts = preprocess_text(input_text) 
    # 단어 사전 생성
    dictionary = corpora.Dictionary([processed_texts])
    # 문서-단어 행렬 생성
    corpus = [dictionary.doc2bow(text) for text in [processed_texts]]
    print(corpus)
    # LDA 모델 훈련
    lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=passes)
    
    # 주제 출력
    #opics = lda_model.print_topics(num_topics=num_topics, num_words=5)

    important_words = []
    
    # 각 주제에서 가장 중요한 3개의 단어 추출
    for topic_num in range(num_topics):
        topic = lda_model.print_topics(num_topics=num_topics, num_words=5)[topic_num][1]
        
        # 각 주제에서 상위 3개의 단어만 추출
        words = [word.split('*')[1].strip(' " ') for word in topic.split(' + ')]
        important_words.append(f"Topic {topic_num}: {', '.join(words)}")
    
    return important_words
    
def hashtag_function(input_text: str) -> str:
    result = topic_modeling(input_text)
    print(result)
    return result
'''
    # 해시태그 ID 가져오기
    url = f"https://graph.facebook.com/v16.0/ig_hashtag_search?user_id={USER_ID}&q={HASHTAG_NAME}&access_token={ACCESS_TOKEN}"
    print(url)
    response = requests.get(url).json()

    print(response)
    return response
    '''