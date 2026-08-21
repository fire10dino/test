import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My AI",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 My AI")
st.caption("A simple AI chatbot powered by OpenAI")

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What would you like to ask?"):

    # Display user's message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user's message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Temporary response
    response = "Hello! Your webpage is working."

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
