import streamlit as st
from langchain_helper import chotu_chain

st.set_page_config(page_title="Chotu the Store Assistant", page_icon="🛍️", layout="centered")
st.title("🧠 Meet Chotu — Your Smart Store Buddy")

question = st.text_input("Talk to Chotu:", placeholder="e.g., How many red t-shirts? or Chotu, tell me a joke!")

if question:
    with st.spinner("Thinking..."):
        response = chotu_chain(question)

    st.header("🗨️ Chotu Says:")
    st.write(response)

st.markdown("---")
st.markdown("💬 Ask me about inventory, jokes, calculations or anything else you'd ask your real store buddy Chotu.")
