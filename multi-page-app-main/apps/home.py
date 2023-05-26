import streamlit as st

def app():
    st.title(":house_with_garden: Homepage")
    st.write("Welcome to the homepage of the cat and dog image classification application developed by Asmae Adnadane.")
    st.sidebar.success("Select a page above.")
    if "my_input" not in st.session_state:
      st.session_state["my_input"] = ""
    my_input=st.text_input("Please input your name here ", st.session_state["my_input"])
    submit=st.button("Submit")
    if submit:
      st.session_state["my_input"]=my_input
      st.write("Thanks for using our webpage dear ",my_input)