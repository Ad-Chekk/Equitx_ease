import streamlit as st

# Title and description
st.title("My First Streamlit App")
st.write("Welcome to my simple Streamlit app! 🎉")

# Interactive input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")

# Sample visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create some dummy data
data = pd.DataFrame({
    'x': range(1, 101),
    'y': np.random.randint(1, 100, 100)
})

st.line_chart(data)
