import streamlit as st

# Initialize chat history in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to display chat messages
def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Display existing chat messages
display_messages()

# Get user input
if prompt := st.chat_input("Ask me about your travel plans..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Placeholder for AI response
    ai_response = "This is a placeholder response. Your travel planning AI will assist you here."
    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)
