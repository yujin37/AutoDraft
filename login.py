import streamlit as st
import pyrebase
import json

with open("firebase_config.json", "r") as f:
    firebase_config = json.load(f)

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
def login_page():
    
    st.title('AutoDraft')
    st.subheader('Login')
    email = st.text_input("Email")
    pw = st.text_input("Password", type = 'password')
    btn = st.button("Login", key="login_btn")  # key로 고유 ID를 지정


    if btn:
        try:
            user = auth.sign_in_with_email_and_password(email, pw)
            st.success("로그인 성공!")
            st.session_state["logged_in"] = True
            st.session_state["user"] = user
            st.session_state["page"] = "home"
            st.rerun()
        except Exception as e:
            st.error(f"로그인 실패: {e}")
    #if "user" in st.session_state:
        #if st.button("Logout"):
        #    del st.session_state["user"]
        #    st.success("로그아웃 완료")

