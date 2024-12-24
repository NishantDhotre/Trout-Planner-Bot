import streamlit as st

st.title("Trip Planner")

# Initialize session state for messages
if 'messages' not in st.session_state:
    st.session_state.messages = []


# Function to display chat messages
def display_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


# Display existing chat messages
display_messages()

# Get user input
if prompt := st.chat_input("How can I assist you with your day tour planning?"):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Generate assistant response (placeholder)
    response = f"Let's plan your day in {prompt}!"

    # Add assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)
