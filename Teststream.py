import streamlit as st
import pandas as pd
import re

def extract_numbers(text, keyword):
    try:
        result = re.search(f'(\d+)\s*{keyword}', text, re.IGNORECASE)
        return result.group(1)
    except AttributeError:
        return None

def process_data(df):
    df['Package size'] = df['Drug Name'].apply(lambda x: extract_numbers(x, 'FCT'))
    df['Strenght'] = df['Drug Name'].apply(lambda x: extract_numbers(x, 'Mg'))
    return df


st.title('Sales Market and Drug Name File Upload')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    st.write(data)

    if st.button('Process Data'):
        data = process_data(data)
        st.write(data)
