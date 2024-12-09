# AutoDraft 
블로그 작성을 도와주는 에이전트

## 파일 구성(24.12.9 기준)
- style_model.py : 사용자 표현 특징을 캐치해서 저장하는 모델
- model.py : style_model에서 저장한 특징들을 가져와서 그 특징을 기반으로 내용 생성 모델
- title_model.py : 제목 생성 모델