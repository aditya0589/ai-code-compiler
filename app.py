import streamlit as st
from code_executer import execute_code 

st.title("AI Python Compiler")
st.subheader("Built by Aditya")


with st.form("my_form"):
    code = st.text_area(
        "Code here",
        height=400,
        placeholder="print('Hello, World')"
    )
    submitted = st.form_submit_button("Run Code")

if submitted:
    try:
        result = execute_code(code)
    except Exception as e:
        result = f"⚠️ Error while executing: {e}"
    

    st.text_area(
        "Output",
        height=150,
        value=result
    )

with st.sidebar:
    st.title("ABOUT AI COMPILER")
    st.markdown("""
    This AI compiler was developed by ***Y.Aditya***  
    
    **Working:**  
    The compiler is powered by Google Gemini (gemini-1.5-flash LLM model),
    served via the LangChain API.  
    It uses an AI agent to read and understand the written code, then execute it using the Python REPL tool.    
    
    **How to use:**  
    1. Type your code in the input box provided (either it can be code or natural language text) 
    2. Click the ***Run Code*** button  
    3. The agent will review and execute your code  (or convert and execute if its natural language)
    4. Output will be displayed in the ***Output*** box below  
    """)


