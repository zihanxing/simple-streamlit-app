import streamlit as st
from transformers import pipeline

st.title('Translate Chinese to English')

st.markdown("""
<style>
body {
    color: #fff;
    background-color: #111;
}
.stTextInput>div>div>input, .stTextArea>div>div>textarea {
    color: #4F8BF9;
}
.stButton>button {
    border-radius:20px;
    border:1px solid #4F8BF9;
    color: #fff;
    background-color: #4F8BF9;
}
.stMarkdown>div>p {
    color: #4F8BF9;
}
</style>
""", unsafe_allow_html=True)

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")

text_to_translate = st.text_area("Please type input: (Example: 你好，很高兴认识你)", value='', height=250, max_chars=500)

if st.button('Translate'):
    if text_to_translate:
        translation = translator(text_to_translate, max_length=400)[0]['translation_text']
        st.write("Translated result:", translation)
    else:
        st.write("Please enter some text to translate.")
