import streamlit as st
import sidebar
import requests

def home():
    sidebar.sidebar_menu()
    st.title('AutoDraft')
    st.subheader('Total Agent')
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

        # 버튼이 눌렸는지 확인
        if st.button('Generation') and text:
            if blog_gen:
                st.text("블로그 생성 기능 작동")
                with st.spinner('블로그 생성 중...'):
                    response_1 = requests.post(
                    "http://127.0.0.1:8000/blog", json={"input_text": text, "user": text}

                    )
                    if response_1.status_code == 200:
                        processed_text_1 = response_1.json()
                        #processed_text = response.json()["processed_text"]
                        st.write("처리된 텍스트:", processed_text_1)
                    else:
                        st.write("API 호출 실패")
            if summary_gen:
                st.text('요약 기능 작동')
                with st.spinner('요약 중...'):
                    response_2 = requests.post(
                    "http://127.0.0.1:8000/summary", json={"input_text": text}

                    )
                    if response_2.status_code == 200:
                        processed_text_2 = response_1.json()
                        #processed_text = response.json()["processed_text"]
                        st.write("처리된 텍스트:", processed_text_2)
                    else:
                        st.write("API 호출 실패")
            if hashtag_gen:
                st.text('해시태그 추천 기능 작동')
                with st.spinner('해시태그 추천 중...'):
                    response_3 = requests.post(
                    "http://127.0.0.1:8000/hashtag", json={"input_text": text}

                    )
                    if response_3.status_code == 200:
                        processed_text_3 = response_1.json()
                        #processed_text = response.json()["processed_text"]
                        st.write("처리된 텍스트:", processed_text_3)
                    else:
                        st.write("API 호출 실패")
        

if __name__ == "__main__":
    home()
