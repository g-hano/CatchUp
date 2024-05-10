import streamlit as st
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI

from llama_index.core.memory import ChatMemoryBuffer
from tools import Report, InternetSearch, wikipedia_search

report_tool = FunctionTool.from_defaults(fn=Report, 
                                         name="Report", 
                                         description="""Useful when you are done with analysis and want to save the final version of the report.""")
internetSearch_tool = FunctionTool.from_defaults(fn=InternetSearch,
                                                 name="InternetSearch",
                                                 description="""Utilizes Search Engine API to find information on the internet. This tool is handy for general inquiries or topics that may not be as extensively covered on Wikipedia.""")  
wikipedia_tool = FunctionTool.from_defaults(fn=wikipedia_search,
                                            name="wikipedia_search",
                                            description="""Searches Wikipedia based on user input. It is useful when user asks something more scientific or specific""")
st.set_page_config(page_title="Catch-Up",
                   page_icon="🍅")
st.title("Catch-Up E-Commerce Agent🤖")

if "API_KEY" not in st.session_state:
    st.session_state["API_KEY"] = ""

with st.sidebar:    
    user_api = st.text_input("OpenAI API key here")
    if st.button("Insert"):
        with st.spinner(text="Inserting API Key"):
            st.write(f"API Key {user_api}")
            st.session_state["API_KEY"] = user_api


#? ------------------
import base64
def get_base64_of_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background_image(image_file):
    base64_image = get_base64_of_file(image_file)
    background_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_image}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)
set_background_image("small.jpg")
#? ------------------

with open("newprompt.txt", "r") as f:
    prompt = f.read()
llm = OpenAI(model="gpt-3.5-turbo", api_key=st.session_state["API_KEY"])
#llm = Ollama(model="llama3", request_timeout=360)
agent = ReActAgent.from_tools(llm=llm,
                               max_iterations=20,
                               tools=[report_tool, internetSearch_tool, wikipedia_tool],
                               verbose=True,
                               memory=ChatMemoryBuffer.from_defaults(llm=llm),
                               chat_history=[
                                   {"role":"system", "content": prompt}])



country = st.text_input("What country you want to find best products for?")
text = f"""I want you to find the best products to sell in {country}, after you find enough information give me an analysis for the best possible selling products in {country} market. Make sure the analysis is vert detailed and structered in markdown format."""

if country:
    with st.spinner(text="Searching Internet for Analyze"):
        llm_answer = agent.chat(text)
        st.write(llm_answer.response)
            
        st.download_button(label="Download", data=str(llm_answer), 
                        file_name="CatchUp.txt")