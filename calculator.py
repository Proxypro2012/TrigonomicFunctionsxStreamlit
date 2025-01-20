import streamlit as st
import time
import math

st.title("Trigonometric Functions Calculator")

options = ["tan", "sin", "cos", "sec", "cot", "cosec"]
selected_operation = st.selectbox("Select a trigonometric function: ", options)

value = st.text_input("Input an angle in degrees: ")

if value == "":
    st.info("Please enter a value")
else:
    if any(char.isalpha() for char in value):
        st.info("Please refrain from inputting letters")
    else:
        try:
            # Convert input to a float
            angle = float(value)
            # Convert degrees to radians
            radians = math.radians(angle)

            # Calculate the result
            if selected_operation == "tan":
                result = math.tan(radians)
            elif selected_operation == "sin":
                result = math.sin(radians)
            elif selected_operation == "cos":
                result = math.cos(radians)
            elif selected_operation == "sec":
                result = 1 / math.cos(radians) if math.cos(radians) != 0 else float("inf")
            elif selected_operation == "cosec":
                result = 1 / math.sin(radians) if math.sin(radians) != 0 else float("inf")
            elif selected_operation == "cot":
                result = 1 / math.tan(radians) if math.tan(radians) != 0 else float("inf")
            else:
                result = None

            # Display the result
            if result is not None:
                st.write(f"The result of {selected_operation}({angle}°) is: {result:.6f}")
            else:
                st.error("Invalid operation selected")

        except ValueError:
            st.error("Invalid input. Please enter a numeric value.")

if st.button("Help?"):
    st.info("Try inputting a trigonometric function and a numeric value.")
    time.sleep(1)
    st.info("Credits: This site was made by Kabir Tiwari")