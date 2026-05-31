from Chatbot_backend import chatbot
from langchain_core.messages import HumanMessage
import streamlit as st

# st.session_state -> dict -> dont erase content on display enter
CONFIG = {'configurable':{'thread_id':'thread-1'}} 


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# {'role':'user','content':'hi'}
# {'role':'assistant','content':'hello'}

# with st.chat_message('user'):
#     st.text('hi')

# with st.chat_message('assistant'):
#     st.text('how can i help you') 

user_input = st.chat_input('Type here: ')

if user_input:
    # first add message to message history
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    
    # first add message to message history
    
    with st.chat_message('assistant'):
       ai_message = st.write_stream(
           message_chunk.content for message_chunk,metadata in chatbot.stream(
            {'messages':[HumanMessage(content=user_input)]},
            config = CONFIG,
            stream_mode='messages' 
        )
    )
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})






