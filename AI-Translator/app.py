import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 AI Language Translator")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

source_lang = st.selectbox("From", list(languages.keys()))
target_lang = st.selectbox("To", list(languages.keys()))

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translated Text:")
        st.write(translated)
    else:
        st.warning("Please enter text")