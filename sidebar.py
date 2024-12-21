import streamlit as st
import login
import signup
# 로그아웃 함수
def logout():
    st.session_state["logged_in"] = False
    st.session_state["page"] = "home"
    st.rerun()

def sidebar_menu():
    # 사이드바에 기본 페이지 링크를 자동으로 표시
    st.sidebar.title("Member Login")
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        st.sidebar.success("로그인 중입니다.")
        
        # 로그아웃 버튼
        if st.sidebar.button("Logout"):
            logout()  # 로그아웃 처리 후 세션 리셋
    else:
        # 로그인 버튼
        if st.sidebar.button("Login"):
            st.session_state["page"] = "login"
        
        # 회원가입 버튼
        if st.sidebar.button("SignUp"): 
            st.session_state["page"] = "signup"

    if st.session_state.get("page") == "login":
        login.login_page()  # login.py 파일의 로그인 페이지 함수 호출
    else:
        st.write("홈 화면입니다. 로그인 후 맞춤형 콘텐츠를 이용하세요.")
    if st.session_state.get("page") == "signup":
        signup.signup_page()