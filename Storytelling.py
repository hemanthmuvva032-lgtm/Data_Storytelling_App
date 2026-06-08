import streamlit as st
import pandas as pd
import plotly.express as px

st.title("IPL Data Storytelling App")

# Load Dataset
url = "https://raw.githubusercontent.com/AP-State-Skill-Development-Corporation/Datasets/master/Data%20Analysis/Advertising.csv"
df = pd.read_csv(url)

# Story 1
st.header("Story 1: TV Advertising Impact")

st.write("""
This story explores how TV advertisement spending influences product sales.
Higher TV spending generally results in higher sales.
""")

fig1 = px.scatter(
    df,
    x="TV",
    y="sales",
    title="TV Advertisement vs Sales"
)

st.plotly_chart(fig1)

# Story 2
st.header("Story 2: Distribution of TV Spending")

st.write("""
This chart shows how companies distribute their TV advertisement budgets.
""")

fig2 = px.histogram(
    df,
    x="TV",
    title="Distribution of TV Advertisement Spending"
)

st.plotly_chart(fig2)

# Conclusion
st.header("Conclusion")

st.success("""
TV advertisement spending has a strong positive impact on sales.
Companies investing more in TV advertising generally achieve higher sales.
""")