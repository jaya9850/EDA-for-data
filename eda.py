import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Simple EDA App", layout="centered")
st.title("📊 Simple EDA Web App")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Basic Info")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    st.write("Column Types:")
    st.write(df.dtypes)

    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if numeric_cols:
        st.subheader("📉 Histogram")
        col = st.selectbox("Select a column", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)

        st.subheader("🔁 Correlation Heatmap")
        fig2, ax2 = plt.subplots()
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax2)
        st.pyplot(fig2)
    else:
        st.warning("No numeric columns found for visualization.")
else:
    st.info("Upload a CSV file to begin.")
