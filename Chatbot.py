from openai import OpenAI
import streamlit as st
from PIL import Image

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("Cartoon Memories")
st.caption("🚀 AI-Powered Cartoon Video Maker for Memories")
st.write("""
    ### Transform Your Memories into Cartoon Stories
    Imagine turning your travel snapshots, cherished personal moments, and significant life events into captivating cartoon versions, ready to weave into stories or feeds for social media sharing. Start creating your cartoon memories today and bring a new dimension to your stories!
    """)
st.markdown("""
    <img src="https://i.ibb.co/zZ2w8CX/DALL-E-2024-02-27-23-17-53-Create-an-image-in-the-style-of-a-bright-and-colorful-anime-similar-to-th.webp" width="50%">
""", unsafe_allow_html=True)

# 检查是否已经设置了OpenAI API密钥
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Upload the picture and type the headline below"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

# 允许用户上传图片
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # 显示上传的图片
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # 调用DALL·E模型生成卡通版本的图片
    if st.button('Generate Cartoon Version'):
        try:
            # 初始化OpenAI客户端
            OpenAI.api_key = openai_api_key
            
            # 将上传的图片转换为DALL·E可以接受的格式（如果需要的话）
            # 注意：这个示例不包括这一步，因为它依赖于你如何处理和传递图片到DALL·E

            # 调用DALL·E生成卡通版本的图片
            # 这里需要替换为调用DALL·E的代码，以下为示意性的伪代码
            response = OpenAI.Image.create(
                # 这里添加调用DALL·E的参数，如图片转换的具体要求
                prompt="a cartoon version of this photo",
                n=1,
                size="1024x1024"
            )

            # 假设`response`中包含了生成的图片URL或直接是图片的二进制数据
            # 展示生成的卡通图片
            # 注意：根据你如何接收DALL·E的输出，这里的代码可能需要调整
            generated_image_url = response['data'][0]['url']  # 假设URL
            st.image(generated_image_url, caption='Cartoon Version.')

        except Exception as e:
            st.error(f"Error generating cartoon version: {e}")