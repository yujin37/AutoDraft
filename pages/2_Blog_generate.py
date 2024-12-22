import streamlit as st
import requests
import sidebar

def blog_generate():
    sidebar.sidebar_menu()
    st.title('AutoDraft')
    st.subheader('Blog generate')
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("로그인 후 블로그 생성 기능을 이용할 수 있습니다.")
        return  # 로그인 안 되어 있으면 함수 종료
    else:
        #st.text('내용을 입력하면 블로그 형식으로 작성해줍니다.')
        text = st.text_area(label="내용을 입력하면 블로그 형식으로 작성해줍니다.", placeholder="내용을 입력하세요")
        topics =["Event_recap", "Informative", "Analysis", "Problem_solving", "Tutorial", "Developer_Experience",
                 "Tech_trends", "Tech comparison", "Project update", "Development Philosophy"]
        selected_topic = st.selectbox("Selected topic", topics)
        user = str(st.session_state["user"]['email'])
        if st.button("Generate") and text :
            response = requests.post(
                "http://127.0.0.1:8000/blog", json={"input_text": text, "topic": selected_topic, "user": user}

            )

            if response.status_code == 200:
                processed_text = response.json()
                #processed_text = response.json()["processed_text"]
                st.write("처리된 텍스트:", processed_text)
            else:
                st.write("API 호출 실패")


if __name__ == "__main__":
    blog_generate()
