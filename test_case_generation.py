import openai
import streamlit as st


def gpt3_chatbot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def gpt3_echatbot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def gpt3_pchatbot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def gpt3_achatbot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

with st.sidebar:
    key_input = st.text_input('Enter your secret Key')

openai.api_key = key_input

st.title("AI for Generating Test Cases")
st.write("This is a AI developed by Sneha D A, Bhava, Maharnav Sahu of VIT which generates test cases of every use case you ask, can also be used to clarify educational doubts with it.")

user_input = st.text_input("Type your message here and hit Enter:")

if user_input:
    chatbot_response = gpt3_chatbot(f"{user_input} (Create test cases for each use case given, also write the REGEX without fail for the same if the test needs a REGEX)")
    st.write(chatbot_response)
st.subheader("Choose the use case")
genre = st.radio( "",('E-mail ID', 'Phone no'))
if genre == 'E-mail ID':
    text_ebox =  st.text_input("Type the Email-ID and hit enter to validate")
    if text_ebox:
        chatbot_email_response = gpt3_echatbot("The email id given by the user is "+ text_ebox + " ,check whether this is a valid mail id or not Based on REGEX and the test cases for mail id. JUST SAY VALID OR INVALID, if INVALID say why it is not.")
        st.write(chatbot_email_response)
if genre == 'Phone no':
    text_pbox =  st.text_input("Type the phone number and hit enter to validate")
    if text_pbox:
        chatbot_phno_response = gpt3_pchatbot("The Indian Phone number given by the user is "+ text_pbox + "check whether this is a valid indian phone number or not Based on REGEX and the test cases for indian phone number. JUST SAY VALID OR INVALID, if INVALID say why it is not.")
        st.write(chatbot_phno_response)

st.subheader("Ask us anything")
any_input = st.text_input("Type your question here and hit Enter :")
if any_input:
    chatbot_aresponse = gpt3_achatbot(f"{any_input} (Answer with respect to Object oriented analysis and design)")
    st.write(chatbot_aresponse)
