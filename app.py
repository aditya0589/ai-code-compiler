import streamlit as st
from code_executer import execute_code 

st.title("AI Python compiler")
st.subheader("Built by Aditya")

with st.form("my_form"):
    code = st.text_area(
        "Code here",
        height=400,
        placeholder="print('Hello, World')"
    )

    submitted = st.form_submit_button("run code")


    result = execute_code(code)
    output_box = st.text_area(
    "output",
    height=100,
    value=result
    )

with st.sidebar:
    st.title("ABOUT AI COMPILER")
    st.markdown("""
    This AI compiler was developed by ***Y.Aditya***  
                
    **Working:**  
    The compiler is powered by google gemini (gemini-1.5-flash LLM model),
    served via the langchain API.  
    It uses an AI agent to read and understand the written code. Then execute it using the python REPL tool
    provided to it.  
    The AI agent understands the code and automatically debugs any syntax or logical errors
    which arise in the code. so that it gives an accurate result even for error-riden code.  
                
    **How to use:**  
    1. type your code in the input box provided
    2. click the ***run code*** button
    3. The agent will review, debug and then execute your code.
    4. Output will be displayed in the ***output*** box below.
    """)
