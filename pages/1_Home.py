import streamlit as st
import sidebar

def home():
    sidebar.sidebar_menu()
    
    st.title("블로그 작성 에이전트")  # 제목 설정
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

    #if text:
        # FastAPI API 호출
        #response = requests.post(
        #    "http://127.0.0.1:8000/summary", json={"input_text": text}
        #)
        
        #if response.status_code == 200:
        #    processed_text = response.json()
        #    #processed_text = response.json()["processed_text"]
        #    st.write("처리된 텍스트:", processed_text)
        #else:
        #    st.write("API 호출 실패")

if __name__ == "__main__":
    home()
