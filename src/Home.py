import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="🇨🇳", page_title="ChatBot")


#Contact
with st.sidebar.expander("Contact",expanded=True):

    st.write("**GitHub:**",
"[adam86546853/chatbot](https://github.com/Adam86546853/Robby-chatbot)")

    st.write("**Mail** : adam86546853@gmail.com")
    st.write("**Created by adam86546853**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>🇨🇳 LLM QA(智能推荐算法深圳组)</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:left;'> 
    LLM QA: Empowering langchain and streamlit to support PDF, TXT, CSV, and YouTube transcript!</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#RPages
st.subheader("Discover")
st.write("""
- **Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
- **Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
""")
st.markdown("---")


#Contributing
st.markdown("### Contribute")
st.markdown("""
- **Feel free to contribute and help me make it even more data-aware!**
""", unsafe_allow_html=True)





