import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

st.title("Find the Largest Number")
st.write("Made by Devjeet Haldar")

a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

if st.button("Find the Largest Number"):
    result = find_largest(a, b, c)
    st.write("The largest number is:", result)
