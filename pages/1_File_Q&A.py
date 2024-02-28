import streamlit as st

# 使用 Streamlit 的標題和文本展示功能
st.title("Welcome to ToonTales, Cartoon Memories")

st.write("""
An innovative AI-powered cartoon video maker designed to breathe new life into your memories. Transforming your photos and videos into captivating cartoon stories, perfect for sharing on social media.
""")

st.header("Mission Statement")
st.write("To foster creative and private expression of daily memories, transforming personal moments into engaging visual stories for easy sharing and enhanced social interaction.")

st.header("Target Audience")
st.write("Anyone who loves to travel, create memories, and share their daily lives with others. Whether you're someone who loves capturing every moment or someone who cherishes privacy but still wants to share special occasions in a unique way, ToonTales offers an easy, engaging solution for all.")

st.header("Frequently Asked Questions (FAQ)")

# 使用 Markdown 渲染 HTML 內容
st.markdown("""
- **What problems does ToonTales address?**  
ToonTales makes it easy to share unforgettable trips, ceremonies, and simple joys, breathing life into past days and making sharing effortless.

- **How is ToonTales different from other picture or video editing tools?**  
Unlike other tools that offer generic edits, ToonTales lets users influence the story's nature and tone by specifying words or moods.

- **Who can benefit from using ToonTales?**  
Anyone who loves making memories and sharing them with others, from avid travelers to social media enthusiasts.

- **How do I start using ToonTales?**  
Just upload your photos or videos, specify your desired story's mood or tone, and let our AI do the rest.

- **Can I customize my cartoon stories?**  
Yes! ToonTales is built on the principle of personalization. You're in control of how your stories are told.

- **Is ToonTales suitable for private individuals?**  
Absolutely. ToonTales values privacy and creative expression, suitable for both public sharing and private memories.
""", unsafe_allow_html=True)

st.write("Join us, and let's make every memory unforgettable with ToonTales.")