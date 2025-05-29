from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
#from langchain.memory import BufferMemory
#from langchain.chains import LLMChain
import os
def get_chat_response(prompt,memory,openai_api_key):
    model=ChatOpenAI(model="deepseek-chat",openai_api_key=openai_api_key,
                     base_url="https://api.deepseek.com/v1")  # DeepSeek的API地址

    chain = ConversationChain(llm=model, memory=memory)
    #使用对话链的好处是能够帮助我们自动加入记忆，不需要我们动手做
    response=chain.invoke({"input":prompt})
    return response["response"]
#memory = ConversationBufferMemory(return_messages=True)
#print(get_chat_response("牛顿提出过哪些知名的定律",memory,os.getenv("DEEPSEEK_API_KEY")))
#print(get_chat_response("我上一个问题是什么",memory,os.getenv("DEEPSEEK_API_KEY")))