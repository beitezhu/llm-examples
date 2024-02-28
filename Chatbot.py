from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Cartoon Memories")
st.caption("🚀 AI-Powered Cartoon Video Maker for Memories")
st.write("""
    ### Transform Your Memories into Cartoon Stories
    Imagine turning your travel snapshots, cherished personal moments, and significant life events into captivating cartoon versions, ready to weave into stories or feeds for social media sharing. Start creating your cartoon memories today and bring a new dimension to your stories!
    """)
st.markdown("""
    <img src="https://i.ibb.co/zZ2w8CX/DALL-E-2024-02-27-23-17-53-Create-an-image-in-the-style-of-a-bright-and-colorful-anime-similar-to-th.webp" width="50%">
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
