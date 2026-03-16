import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.header("Streamlit 주요 UI 요소 데모")

st.subheader("텍스트 요소")
st.text("이것은 일반 텍스트입니다.")
st.markdown("**마크다운** _스타일링_ 지원!")
st.code("print('Hello, Streamlit!')", language="python")
st.latex(r"E=mc^2")

st.subheader("데이터 표시")
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=['A', 'B', 'C']
)
st.dataframe(df)
st.table(df.head(3))

st.subheader("차트")
st.line_chart(df)
st.bar_chart(df)

st.subheader("입력 위젯")
name = st.text_input("이름을 입력하세요:")
age = st.number_input("나이", min_value=0, max_value=120, value=25)
agree = st.checkbox("동의합니다")
option = st.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.button("버튼")

st.subheader("슬라이더와 날짜")
value = st.slider("값을 선택하세요", 0, 100, 50)
date = st.date_input("날짜를 선택하세요")

st.subheader("파일 업로드")
uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file is not None:
    st.success(f"업로드된 파일: {uploaded_file.name}")

st.subheader("알림/상태")
st.success("성공 메시지 예시")
st.info("정보 메시지 예시")
st.warning("경고 메시지 예시")
st.error("에러 메시지 예시")
with st.spinner("로딩 중..."):
    import time
    time.sleep(1)
st.balloons()
