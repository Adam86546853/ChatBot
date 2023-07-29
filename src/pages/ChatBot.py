import os
import streamlit as st
from io import StringIO
import re
import sys
from modules.history import ChatHistory
from modules.layout import Layout
from modules.utils import Utilities
from modules.sidebar import Sidebar
from modules.chatbot import Chatbot

#To be able to update the changes made to modules in localhost (press r)
def reload_module(module_name):
    import importlib
    import sys
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
    return sys.modules[module_name]

history_module = reload_module('modules.history')
layout_module = reload_module('modules.layout')
utils_module = reload_module('modules.utils')
sidebar_module = reload_module('modules.sidebar')

ChatHistory = history_module.ChatHistory
Layout = layout_module.Layout
Utilities = utils_module.Utilities
Sidebar = sidebar_module.Sidebar

st.set_page_config(layout="wide", page_icon="🇨🇳", page_title="ChatBot")

# Instantiate the main components
layout, sidebar, utils = Layout(), Sidebar(), Utilities()

st.markdown(
    f"""
    <h1 style='text-align: center;'> Ask For ChatBot</h1>
    """,
    unsafe_allow_html=True,
)

user_api_key = utils.load_api_key()

if not user_api_key:
    layout.show_api_key_missing()
else:
    os.environ["OPENAI_API_KEY"] = user_api_key

    # Configure the sidebar
    sidebar.reset_chat_button()
    sidebar.show_options()
    sidebar.about()

    # Initialize chat history
    history = ChatHistory()
    try:
        chatbot = Chatbot(st.session_state["model"], st.session_state["temperature"],None)
        st.session_state["chatbot"] = chatbot
        st.session_state["ready"] = True

        if st.session_state["ready"]:
            # Create containers for chat responses and user prompts
            prompt_container,response_container = st.container(), st.container()

            with prompt_container:
                # Display the prompt form
                is_ready, user_input = layout.prompt_form()

                # Initialize the chat history
                history.initialize(None)

                # Reset the chat history if button clicked
                if st.session_state["reset_chat"]:
                    history.reset(None)

                if is_ready:
                    # Update the chat history and display the chat messages
                    history.append("user", user_input)

                    is_his = not st.session_state["reset_chat"]
                    output = st.session_state["chatbot"].chat_message_history(user_input,is_his)

                    history.append("assistant", output)

            history.generate_messages(response_container)
    except Exception as e:
        st.error(f"Error: {str(e)}")


