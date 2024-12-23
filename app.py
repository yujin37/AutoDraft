import streamlit as st
import sidebar

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def main():
    st.title("AutoDraft")
    if "user" not in st.session_state:
        st.session_state["user"] = None  # 또는 빈 값으로 초기화

    if st.session_state["user"]:
        st.write(f"User logged in: {st.session_state['user']['email']}")
    else:
        st.write("No user logged in.")
    sidebar.sidebar_menu()
    st.write(st.session_state["user"])
    # 기본 페이지를 Home으로 설정
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Home'

if __name__ == "__main__":
    main()
