import requests
import streamlit as st

def get_ollama_response(input_text):
    try:
        response = requests.post(
            "http://localhost:8000/poem/invoke",
            json={'input': {'topic': input_text}}
        )
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get('output', 'No output found')
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit framework
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Write an essay on")

if input_text:
    output = get_ollama_response(input_text)
    if output:
        st.write(output)