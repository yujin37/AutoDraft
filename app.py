import streamlit as st

def main():
    # 기본 제목 설정
    st.title("블로그 작성 에이전트")
    st.write("앱을 실행합니다. 사이드바에서 페이지를 선택하세요.")

    # 사이드바에 기본 페이지 링크를 자동으로 표시
    st.sidebar.success("페이지를 선택하면 에이전트 기능을 이용할 수 있습니다")
    
    # 홈 페이지로 이동하는 버튼
    #st.sidebar.markdown("### 홈으로 이동")
    #if st.sidebar.button("Go to Home"):
    #    st.session_state['page'] = 'Home'  # 홈 페이지로 이동
    #    st.rerun()  # 페이지 새로고침

    # 기본 페이지를 Home으로 설정
    if 'page' not in st.session_state:
        st.session_state['page'] = 'Home'

if __name__ == "__main__":
    main()
