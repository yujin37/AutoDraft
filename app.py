import streamlit as st
import requests
def main():
    st.title("블로그 작성 에이전트")  # 제목 설정
    text = st.text_area("내용을 입력하세요")  # 텍스트 영역 추가
    st.write("입력한 내용:")
    st.text(text)  # 입력된 텍스트 출력

    if text:
        # FastAPI API 호출
        response = requests.post(
            "http://127.0.0.1:8000/summary", json={"input_text": text}
        )
        
        if response.status_code == 200:
            processed_text = response.json()
            #processed_text = response.json()["processed_text"]
            st.write("처리된 텍스트:", processed_text)
        else:
            st.write("API 호출 실패")

if __name__ == "__main__":
    main()
