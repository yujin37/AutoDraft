import streamlit as st
import pyrebase
import json

with open("firebase_config.json", "r") as f:
    firebase_config = json.load(f)

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
def signup_page():
    
    st.title('AutoDraft')
    st.subheader('SignUp')
    email = st.text_input("Email")
    pw = st.text_input("Password", type = 'password')
    btn = st.button("SignUp", key="signup_btn")  # key로 고유 ID를 지정


    if btn:
        try:
            user = auth.create_user_with_email_and_password(email, pw)
            st.success("회원가입 성공!")
            user = auth.sign_in_with_email_and_password(email, pw)
            st.success("로그인 성공!")
            st.session_state["logged_in"] = True
            st.session_state["user"] = user
            st.session_state["page"] = "home"
            
        except Exception as e:
            st.error(f"로그인 실패: {e}")
