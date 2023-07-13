import re
import sys
from io import StringIO, BytesIO
import matplotlib.pyplot as plt
import streamlit as st
from langchain.callbacks import get_openai_callback
from streamlit_chat import message

from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

class PandasAgent :

    @staticmethod
    def count_tokens_agent(agent, query):
        """
        Count the tokens used by the CSV Agent
        """
        with get_openai_callback() as cb:
            result = agent(query)
            st.write(f'Spent a total of {cb.total_tokens} tokens')

        return result
    
    def __init__(self):
        pass

    def get_agent_response(self, uploaded_file_content, query):
        llm = OpenAI()
        pandas_ai = PandasAI(llm, verbose=True)
        response = pandas_ai(data_frame = uploaded_file_content, prompt=query)
        captured_output = '\n'.join(pandas_ai._logs)
        return str(response), captured_output

    def display_agent_thoughts(self,cleaned_thoughts):
        with st.expander("Display the agent's thoughts"):
            st.write(cleaned_thoughts)

    def update_chat_history(self,query, result):
        st.session_state.chat_history.append(("user", query))
        st.session_state.chat_history.append(("agent", result))

    def display_chat_history(self):
        for i, (sender, message_text) in enumerate(st.session_state.chat_history):
            if sender == "user":
                message(message_text, is_user=True, key=f"{i}_user")
            else:
                message(message_text, key=f"{i}")