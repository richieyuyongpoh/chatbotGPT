import openai 
import streamlit as st

  
from streamlit_chat import message

openai.api_key = st.secrets["api_secret"]


def generate_response(prompt):
    chatCompletion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens = 500,
        messages=[
            {"role": "system", "content": "You are a very smart data science professor who can explain data science very well using layman's terms. You won't be able to answer any other questions other than data science related topics."},
            {"role": "user", "content": "What is classification?"},
            {"role": "assistant", "content": "Classification may be defined as the process of predicting class or category from observed values or given data points."},
            {"role": "user", "content": f"{prompt}"}])
    
    message = chatCompletion.choices[0]["message"]["content"]
        
    return message
             
             
             
st.title("ChatBot Demo (using ChatGPT API)")

readme = st.checkbox("readme first")

if readme:

    st.write("""
        This is a chatbot demo using [ChatGPT API](https://platform.openai.com/docs/guides/chat). 
        The web app is hosted on [streamlit cloud](https://streamlit.io/cloud). 
        You may get the codes [HERE](https://github.com/richieyuyongpoh/sentimentalAnalysis). 
        """)
    
    st.write("""
        The bot's behavior has been preset. She is 'a very smart data science professor who can explain data science very well using layman's terms.'
        """)
    

    
    st.write ("For more info, please contact:")

    st.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)

st.write("Instruction:")
st.write("")
st.write("""
    Type your own sentence (short & precise) in the textbox below to chat with the bot.
        """)    
    

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
             
def get_text():
    input_text = st.text_input("You: ","Explain data science in one sentence", key="input")
    return input_text
             
user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
             
if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
