import streamlit as st
import time

st.set_page_config(page_title="DS Visualizer", layout="centered")

st.title("📊 Data Structures Visualizer")

menu = st.sidebar.selectbox(
    "Choose Visualization",
    ["Array", "Stack", "Binary Search"]
)

# ---------------- ARRAY ----------------
if menu == "Array":
    st.header("Array Visualization")

    nums = st.text_input("Enter numbers (comma separated)", "1, 3, 5, 7, 9")
    index = st.number_input("Index to access", min_value=0, step=1)

    try:
        arr = [int(x.strip()) for x in nums.split(",")]

        cols = st.columns(len(arr))
        for i, col in enumerate(cols):
            if i == index:
                col.markdown(
                    f"<div style='padding:15px; background:#4CAF50; color:white; text-align:center'>{arr[i]}</div>",
                    unsafe_allow_html=True
                )
            else:
                col.markdown(
                    f"<div style='padding:15px; background:#eee; text-align:center'>{arr[i]}</div>",
                    unsafe_allow_html=True
                )

    except:
        st.error("Please enter valid numbers.")

# ---------------- STACK ----------------
elif menu == "Stack":
    st.header("Stack Operations")

    if "stack" not in st.session_state:
        st.session_state.stack = []

    value = st.number_input("Value", step=1)

    col1, col2 = st.columns(2)

    if col1.button("Push"):
        st.session_state.stack.append(value)

    if col2.button("Pop"):
        if st.session_state.stack:
            st.session_state.stack.pop()

    st.subheader("Stack (Top at bottom)")
    for item in reversed(st.session_state.stack):
        st.markdown(
            f"<div style='padding:10px; border:1px solid #333; text-align:center'>{item}</div>",
            unsafe_allow_html=True
        )

# ---------------- BINARY SEARCH ----------------
elif menu == "Binary Search":
    st.header("Binary Search Visualization")

    nums = st.text_input("Enter sorted numbers", "1, 3, 5, 7, 9, 11")
    target = st.number_input("Target", step=1)

    try:
        arr = [int(x.strip()) for x in nums.split(",")]

        low, high = 0, len(arr) - 1
        placeholder = st.empty()

        if st.button("Start Search"):
            while low <= high:
                mid = (low + high) // 2

                with placeholder.container():
                    cols = st.columns(len(arr))
                    for i, col in enumerate(cols):
                        if i == mid:
                            col.markdown(
                                f"<div style='padding:15px; background:#FF9800; color:white; text-align:center'>{arr[i]}</div>",
                                unsafe_allow_html=True
                            )
                        else:
                            col.markdown(
                                f"<div style='padding:15px; background:#eee; text-align:center'>{arr[i]}</div>",
                                unsafe_allow_html=True
                            )

                time.sleep(1)

                if arr[mid] == target:
                    st.success(f"Found {target} at index {mid}")
                    break
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                st.error("Target not found")

    except:
        st.error("Invalid input.")
