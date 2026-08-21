import streamlit as st
from openai import OpenAI

# Page settings
st.set_page_config(
    page_title="My AI",
    page_icon="🤖"
)

st.title("🤖 My AI")
st.caption("Powered by OpenAI")

# Connect to OpenAI
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user's message
if prompt := st.chat_input("What would you like to ask?"):

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Ask OpenAI
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = client.responses.create(
                model="gpt-5.6",
                input=st.session_state.messages
            )

            answer = response.output_text

            st.markdown(answer)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
