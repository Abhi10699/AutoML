import streamlit as st
import pandas as pd

st.title("AutoML")

# Upload CSV File

uploaded_file = st.file_uploader("Upload your Dataset file")

if uploaded_file is not None:
  if uploaded_file.type == "text/csv":
    df_csv = pd.read_csv(uploaded_file)
    st.write(df_csv)