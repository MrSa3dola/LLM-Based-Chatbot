import requests

import streamlit as st

st.title("Gemini Bot")

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
        # Call the FastAPI endpoint
        response = requests.post(
            "http://backend:8000/query", json={"messages": st.session_state.messages}
        )
        data = response.json()
        full_response = data.get("response", "")
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
