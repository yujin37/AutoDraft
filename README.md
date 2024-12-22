# AutoDraft 

## 프로젝트 소개
AutoDraft는 개인 PR 시대에 맞춰 다양한 SNS 플랫폼(Facebook, Instagram, Linkedin, Slack, Discord)에서의 **효과적인 콘텐츠 생성**을 지원하는 서비스입니다.  
커뮤니티 참여의 중요성은 높아지는 반면, 콘텐츠 제작은 많은 부담을 동반합니다.  
AutoDraft는 **콘텐츠 생성부터 제목, 해시태그 추천, 요약까지** 한 번에 해결하여 사용자의 부담을 덜어줍니다.  
## 시작 가이드

### Requirements
For building and running the application you need
- Python 3.8 이상  
### Installation

#### Backend
1. FastAPI 설치
```bash
   pip install fastapi uvicorn
```
2. 추가 의존성 설치
```bash
pip install -r requirements.txt
```
3. FastAPI 서버 실행
```bash
uvicorn main:app --reload
```
#### Frontend
1. Streamlit 설치
```bash
pip install streamlit
```
2. Streamlit 앱실행
```bash
streamlit run app.py
```
## 화면 구성
## 주요 기능
- Content Generation

    - 사용자 입력을 기존에 입력되어있는 사용자의 특징을 반영하여 내용 생성
- Hashtag Recommendation

    - 입력 콘텐츠와 연관된 해시태그를 추천하여 SNS에서의 가시성을 극대화.
- Content Title

    - 사용자 입력을 통해 매력적인 콘텐츠 제목을 추천.
- Content Summary

    - 긴 콘텐츠를 요약하여 간결하고 핵심적인 정보를 제공.



## 아키텍처 
