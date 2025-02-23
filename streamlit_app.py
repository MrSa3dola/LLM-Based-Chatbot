import streamlit as st

from gemini import generate_content

st.title("Echo Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I assist you today? 😊"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Stream Gemini's response
        for chunk in generate_content(st.session_state.messages):
            if chunk.text:  # check not None
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")  # Cursor effect
                
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
