from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain_experimental.tools import PythonREPLTool
from langchain.tools import Tool
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

def execute_code(code: str):
    execution_instructions = """
    The input will be a Python code snippet.
    Execute the code in a Python REPL and return ONLY the output.
    If there is an error, return only the error message.
    """

    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=execution_instructions)

    repl_tool = PythonREPLTool()
    python_agent = create_react_agent(
        prompt=prompt,
        llm=ChatGoogleGenerativeAI(temperature=0, model="gemini-1.5-flash"),
        tools=[repl_tool],
    )
    python_agent_executor = AgentExecutor(
        agent=python_agent,
        tools=[repl_tool],
        verbose=True,
        allow_dangerous_code=True,
    )

    result = python_agent_executor.invoke({"input": code})
    return result.get("output", "No output returned.")