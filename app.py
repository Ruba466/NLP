import spacy
import streamlit as st
import pandas as pd

nlp = spacy.load("en_core_web_sm")

st.title("Data Tokenization and Lemmatization")
user_input= st.text_area("Enter your text:")

if st.button("Start"):
    doc = nlp(user_input)
    
    cleaned_tokens=[]
    
    for token in doc :
        if not token.is_stop and not token.is_punct and not token.is_space:
            cleaned_tokens.append((token.text,token.lemma_))

    if cleaned_tokens :
        st.subheader("Cleaned tokens and their Lemmas:")
        df=pd.DataFrame(cleaned_tokens,columns=['Tokens','Lemma'])
        st.table(df)
    else :
        st.warning("No tokens found")