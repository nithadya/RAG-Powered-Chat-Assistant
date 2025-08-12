
import os
import streamlit as st
from llama_index.llms.groq import Groq

# Load Groq API key from environment variable
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# RAG 
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings


def retrieve_generate(prompt):
    llm = Groq(model="llama3-8b-8192", api_key=GROQ_API_KEY)
    response = llm.complete(prompt)

    return response
def rag(prompt):
    documents = SimpleDirectoryReader("./data").load_data()
    Settings.llm = Groq(model="llama3-8b-8192", api_key=GROQ_API_KEY)
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    Settings.num_output = 512
    Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
    index = VectorStoreIndex.from_documents(documents, embed_model=Settings.embed_model, llm=Settings.llm)

    index.storage_context.persist()

    query_engine = index.as_query_engine()
    response = query_engine.query(prompt) 

    return response


st.title(f"**Chat :green[Assistant]** :sparkles:")  # Add emojis and colors to the title

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("Ask any question here !"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display assistant response in chat message container

    response = rag(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})