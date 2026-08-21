import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="My AI",
    page_icon="🤖"
)

st.title("🤖 My AI")
st.caption("Powered by Groq")

# Connect to Groq
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("What would you like to ask?"):

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Ask Groq
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=st.session_state.messages
            )

            answer = response.choices[0].message.content

            st.markdown(answer)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
