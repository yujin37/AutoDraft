import streamlit as st
import sidebar

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
        if st.button('Generation'):
            if blog_gen:
                st.text("블로그 생성 기능 작동")
            if summary_gen:
                st.text('요약 기능 작동')
            if hashtag_gen:
                st.text('해시태그 추천 기능 작동')

if __name__ == "__main__":
    home()
