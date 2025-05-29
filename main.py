from langchain.memory import ConversationBufferMemory
import streamlit as st
from units import  get_chat_response
st.title("克隆chatGpt")
with st.sidebar:
    openai_api_key=st.text_input("请输入OpenAI APIkey:",type="password")
    st.markdown("[获取DeepSeek API密钥](https://platform.deepseek.com/)")
if "memory" not in st.session_state:
    st.session_state["memory"]=ConversationBufferMemory(return_messages=True)
    st.session_state["messages"]=[{"role":"ai","content":"你好，我是你的面试助手，有什么可以帮到你的吗"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])
prompt=st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入你的OpenAI密钥")
        st.stop()
    st.session_state["messages"].append({"role":"human", "content":prompt})
    st.chat_message("human").write(prompt)
    with st.spinner("AI正在思考中，请稍等..."):
        response=get_chat_response(prompt,st.session_state["memory"],openai_api_key)
    msg={"role":"ai","content":response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)