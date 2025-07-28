import streamlit as st
import pandas as pd
import pickle
import os

st.title("AI Visualizer: DataOps & MLOps Demo")

# DataOps: Hiển thị dữ liệu từ CSV
st.header("Data Visualization (DataOps)")
if os.path.exists("/data/input.csv"):
    df = pd.read_csv("/data/input.csv")
    st.write("Data Preview:")
    st.dataframe(df)
    st.line_chart(df.select_dtypes(include=["float64", "int64"]))
else:
    st.write("Please upload input.csv to /data")

# MLOps: Dự đoán AI
st.header("Text Classification (MLOps)")
text = st.text_input("Enter text for sentiment analysis:")
if text:
    try:
        model = pickle.load(open("model.pkl", "rb"))
        prediction = model.predict([text])[0]
        st.write(f"Prediction: {prediction}")
    except:
        st.write("Model not found. Please provide model.pkl")