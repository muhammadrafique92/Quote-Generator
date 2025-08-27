import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

st.title("🧮 Scientific Calculator")

st.write("Enter a mathematical expression below and get the result.")

# Input field
expression = st.text_input("Enter expression (e.g. 2+3*math.sin(1)):")

# Safe evaluation context
allowed_names = {k: v for k, v in math.__dict__.items()}
allowed_names["abs"] = abs
allowed_names["round"] = round

if st.button("Calculate"):
    try:
        # Evaluate using safe dictionary
        result = eval(expression, {"__builtins__": None}, allowed_names)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("### Examples you can try:")
st.code("2+3*4", language="python")
st.code("math.sqrt(25)", language="python")
st.code("math.sin(math.pi/2)", language="python")
st.code("abs(-42)", language="python")
