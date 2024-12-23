import streamlit as st
import sidebar
import requests

def home():
    sidebar.sidebar_menu()
    st.title('AutoDraft')
    st.subheader('Total Agent')
    
    # 로그인 확인
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("블로그 생성 기능이 포함되어 있어 로그인 후 이용 가능합니다.")
        return  # 로그인 안 되어 있으면 함수 종료
    else:
        text = st.text_area("내용을 입력하세요")  # 텍스트 영역 추가
        st.write("입력한 내용:")
        st.text(text)  # 입력된 텍스트 출력

        # 체크박스 상태 확인
        blog_gen = st.checkbox('Blog Generation')
        summary_gen = st.checkbox('Summary Generation')
        hashtag_gen = st.checkbox('Recommend Hashtag')
        user = str(st.session_state["user"]['email'])

        topics = ["event_recap", "informative", "analysis", "problem_solving", "tutorial", 
                  "developer_experience", "tech_trends", "tech_comparison", "project_update", 
                  "development_Philosophy"]
        selected_topic = st.selectbox("Selected topic", topics)

        processed_text_1 = ""  # 블로그 처리 텍스트 변수 초기화
        processed_text_2 = ""  # 요약 처리 텍스트 변수 초기화
        processed_text_3 = ""  # 해시태그 처리 텍스트 변수 초기화

        # 버튼이 눌렸는지 확인
        if st.button('Generation') and text:
            if blog_gen:
                st.text("블로그 생성 기능 작동")
                with st.spinner('블로그 생성 중...'):
                    response_1 = requests.post(
                        "http://127.0.0.1:8000/blog", json={"input_text": text, "topic": selected_topic, "user": user}
                    )
                    if response_1.status_code == 200:
                        processed_text_1 = response_1.json()["content"]
                        st.write("블로그 처리된 텍스트:", processed_text_1)
                    else:
                        st.write("블로그 API 호출 실패")
            
            # 블로그 생성 후, 요약이 요청되면 요약 생성
            if blog_gen and summary_gen and processed_text_1:
                st.text('요약 기능 작동')
                with st.spinner('요약 중...'):
                    response_2 = requests.post(
                        "http://127.0.0.1:8000/summary", json={"input_text": processed_text_1}
                    )
                    if response_2.status_code == 200:
                        processed_text_2 = response_2.json()
                        st.write("요약 처리된 텍스트:", processed_text_2)
                    else:
                        st.write("요약 API 호출 실패")
            
            # 블로그 생성 후, 해시태그 추천이 요청되면 해시태그 생성
            if blog_gen and hashtag_gen and processed_text_1:
                st.text('해시태그 추천 기능 작동')
                with st.spinner('해시태그 추천 중...'):
                    response_3 = requests.post(
                        "http://127.0.0.1:8000/hashtag", json={"input_text": processed_text_1}
                    )
                    if response_3.status_code == 200:
                        processed_text_3 = response_3.json()
                        st.write("해시태그 처리된 텍스트:", processed_text_3)
                    else:
                        st.write("해시태그 API 호출 실패")


if __name__ == "__main__":
    home()
