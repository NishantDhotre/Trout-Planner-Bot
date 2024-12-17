import streamlit as st

# Streamlit chat interface
if 'messages' not in st.session_state:
    st.session_state.messages = []

def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

display_messages()

if prompt := st.chat_input("Ask me about your travel plans..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    ai_response = "This is a placeholder response. Your travel planning AI will assist you here."
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)