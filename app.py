import streamlit as st

def main():
    # Set the app title
    st.title("Basic Calculator App")

    # Input fields for the calculator
    st.header("Enter the Numbers")
    num1 = st.number_input("Enter the first number:", step=1.0, format="%.2f")
    num2 = st.number_input("Enter the second number:", step=1.0, format="%.2f")

    # Dropdown menu for selecting the operation
    operation = st.selectbox(
        "Choose an operation:",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )

    # Perform the calculation when the button is clicked
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
            st.success(f"The result of addition is: {result}")
        elif operation == "Subtraction":
            result = num1 - num2
            st.success(f"The result of subtraction is: {result}")
        elif operation == "Multiplication":
            result = num1 * num2
            st.success(f"The result of multiplication is: {result}")
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
                st.success(f"The result of division is: {result}")
            else:
                st.error("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()
