import openai
import streamlit as st

openai.api_key = "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"

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

st.title("AI for Generating Test Cases")
st.write("This is a AI developed by Sneha D A, Bhava, Maharnav Sahu of VIT which generates test cases of every use case you ask, can also be used to clarify educational doubts with it.")

user_input = st.text_input("Type your message here and hit Enter:")

if user_input:
    chatbot_response = gpt3_chatbot(f"{user_input} (Create test cases for each use case given, also write the REGEX without fail for the same if the test needs a REGEX)")
    st.write(chatbot_response)
