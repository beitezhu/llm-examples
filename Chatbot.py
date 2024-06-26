from openai import OpenAI
import streamlit as st
from PIL import Image
import base64
from pathlib import Path

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.title("Momentoons")
st.caption("🚀 AI-Powered Cartoon Video Maker for Memories")
st.write("""
    ### Transform Your Memories into Cartoon Stories
    Imagine turning your travel snapshots, cherished personal moments, and significant life events into captivating cartoon versions, ready to weave into stories or feeds for social media sharing. Start creating your cartoon memories today and bring a new dimension to your stories!
    """)
st.markdown("""
    <img src="https://i.ibb.co/zZ2w8CX/DALL-E-2024-02-27-23-17-53-Create-an-image-in-the-style-of-a-bright-and-colorful-anime-similar-to-th.webp" width="50%">
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Upload the picture and type the headline below"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 允许用户上传图片
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
moment_style = st.text_input("What style do you want your moment to be inspired by eg: Japanese Ghibli, Simpsons, Batman, Pokemon, Marvel")
narration_voice = st.selectbox("What voice would you like to use", ("alloy", "echo", "fable", "onyx", "nova", "shimmer"))


if uploaded_image is not None:
    # 显示上传的图片
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    # 将图片转换为base64编码
    uploaded_image.seek(0)
    img_binary = uploaded_image.read()
    base64_image_data = base64.b64encode(img_binary).decode('utf-8')

    # 调用 gpt-4 & dall-e-3 模型生成卡通版本的图片
    if st.button('Generate Cartoon Version'):
        # 建立 OpenAI 客户端
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()
        client = OpenAI(api_key=openai_api_key)

        try:
            # 初始化OpenAI客户端
            OpenAI.api_key = openai_api_key
            
            # 将上传的图片转换为 gpt-4 可以接受的格式（如果需要的话）

            # 调用 gpt-4 描述這張圖片
            response = client.chat.completions.create(
                #  model="gpt-4",
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe the image detailed, include number of people."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": "data:image/jpeg;base64," +  base64_image_data,
                                }
                            },
                        ],
                    }
                ],
                max_tokens=300,                
            )

            # 取得 gpt-4 生成的描述
            img_description = response.choices[0].message.content
            img_description = img_description[:2000]
            print("Image description: " + img_description)

            st.write(img_description)

            # 调用 dall-e-3 生成卡通版本的图片
            response = client.images.generate(
                # 这里添加调用DALL·E的参数，如图片转换的具体要求
                model="dall-e-3",
                prompt="Create a cartoon inspired by " + moment_style + " style: " + img_description,
                n=1,
                size="1024x1024"
            )
            
            # 显示生成的卡通版本的图片
            generated_image_url = response.data[0].url
            st.image(generated_image_url, caption=moment_style + " version")

            # 调用 gpt-4 描述這張圖片
            response = client.chat.completions.create(
                #  model="gpt-4",
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "In the style of " + moment_style + ". Be fun and cinematic and narrate the moment felt by the following description in 40 words for social media. Here is the description: " + img_description},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": "data:image/jpeg;base64," +  base64_image_data,
                                }
                            },
                        ],
                    }
                ],
                max_tokens=300,                
            )

            stylized_description = response.choices[0].message.content

            st.write(stylized_description)

            speech_file_path = "speech.mp3"
            audio_response = client.audio.speech.create(model="tts-1", voice="alloy", input=response.choices[0].message.content)
            audio_response.stream_to_file(speech_file_path)
            audio_file = open(speech_file_path, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button(label="Download Speech",
                                data=audio_bytes,
                                file_name="speech.mp3",
                                mime="audio/mp3")


        except Exception as e:
            st.error(f"Error generating stylized version: {e}")
