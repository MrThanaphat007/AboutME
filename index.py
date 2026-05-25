import streamlit as st

st.set_page_config(
    page_title="My Personal Space",
    page_icon=":star:",
    layout="centered",
)

st.title("Benvenuti!")
st.subheader("นี่คือส่วนที่แนะนำตัวของผม")
st.write("---")


col1, col2 = st.columns([1,2])

with col1:
    st.image("MyFace.jpg", caption="That's me")

with col2:
    st.markdown("""
        ### **Su di me**
        * **ชื่อ:** SonoThanaphat
        * **สถานะ:** กำลังเตรียมตัวเข้ามหาลัย
        * **Goal:** ต้องการที่จะเรียนด้าน Digital Humanities
   """)    
st.write("---")

st.header("Skills and Passions")

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.info("**Tech**\n*Python(Beginner)")
with col_b:
    st.success("**Languages**\n* Thai, Britist and Italian(Studying)")
with col_c:
    st.warning("**Interests**\n* Old money and Europe") 

st.write("---")


st.header("Contact Me")
st.text("Email: thamnakthanaphat@gmail.com")


st.caption("WinterBourne")


