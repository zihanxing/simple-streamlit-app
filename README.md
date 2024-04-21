# Week 9 Mini-Project
## Developed by
Zach Xing

## Project Specifications
- Construct a web interface using Streamlit.
- Integrate with a freely accessible LLM (from Hugging Face).
- Make the model accessible online through either Streamlit or another comparable service.

## Application Description
### Capabilities
This application, designed using Streamlit, facilitates English translations from Chinese text. It leverages an open-source LLM, specifically the `Helsinki-NLP/opus-mt-zh-en` model from the `transformers` library. Users can test the functionality by inputting a sentence, pressing the "translate" button, and viewing the English translation displayed below the input area.

### Access Link
The application is hosted on Streamlit at the following URL: https://zs148-ids721-week9-btkkfloe3a4qjpqtfgf6mn.streamlit.app/

## Implementation Steps
### Required Installations
Before launching the app, install the following essential packages:
```
sudo pip install streamlit transformers tensorflow sentencepiece
```

### Building the Streamlit Application
Develop a Python script to perform the translation task:
```python
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")

text_to_translate = st.text_area("Please type input: (Example: 你好，很高兴认识你)", value='', height=250, max_chars=500)

if st.button('Translate'):
    if text_to_translate:
        translation = translator(text_to_translate, max_length=400)[0]['translation_text']
        st.write("Translated result:", translation)
    else:
        st.write("Please enter some text to translate.")
```
To run a local test of the app, execute:
```
sudo streamlit run streamlit_app.py
```
For adapting the app to different translation tasks, consult the [Hugging Face model repository](https://huggingface.co/models).

### Deployment Through Streamlit
To prepare for deployment, compile all necessary dependencies into a `requirements.txt` file. After uploading the local project to a GitHub repository, link the repository through your Streamlit account for deployment.