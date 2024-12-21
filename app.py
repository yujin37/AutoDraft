import streamlit as st
import sidebar

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def main():
    st.title("블로그 작성 에이전트")
    #st.write("앱을 실행합니다. 사이드바에서 페이지를 선택하세요.")
    sidebar.sidebar_menu()
    
    # 기본 페이지를 Home으로 설정
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Home'

if __name__ == "__main__":
    main()
