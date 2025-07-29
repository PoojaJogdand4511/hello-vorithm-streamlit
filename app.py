import streamlit as st

st.title("Hello Vorithm 👋")

# User input
name = st.text_input("Enter your name:")

# Button
if st.button("Greet Me"):
    if name:
        st.success(f"Hello, {name}! You're doing great 🚀")
    else:
        st.warning("Please enter your name first.")
