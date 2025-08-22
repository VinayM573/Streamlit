# import streamlit as st
# import requests
# import httpx

# API_URL = "http://localhost:8000//api/generate"
# # INFO_URL = "http://localhost:8000/get_info"

# try:
#     info = requests.get(INFO_URL)
#     info_details = info.json()
# except Exception as e:
#     st.error(f"Failed to fetch model info: {e}")
#     info_details = {"model_name": "Unknown", "total_chunks": "N/A"}

# st.set_page_config(page_title="AI Chatbot", layout="wide")
# st.title("🧠 AI Chatbot (Streamlit + FastAPI)")

# with st.sidebar:
#     st.markdown(f"## Model Info: <span style='color:green'>{info_details['model_name']}</span>", unsafe_allow_html=True)
#     st.markdown(f"## Total Chunks: <span style='color:blue'>{info_details['total_chunks']}</span>", unsafe_allow_html=True)

#     if st.button("Clear Chat"):
#         st.session_state.messages = []

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# query = st.chat_input("Type your question here...")

# if query:
#     st.chat_message("user").markdown(query)
#     st.session_state.messages.append({"role": "user", "content": query})

#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""

#         try:
#             spinner = st.spinner("Waiting for response...")
#             spinner.__enter__()

#             with httpx.stream("POST", API_URL, json={"query": query}, timeout=600.0) as r:
#                 sources = r.headers.get("X-Sources")

#                 stream = r.iter_text()
#                 try:
#                     first_chunk = next(stream)
#                     full_response += first_chunk
#                     message_placeholder.markdown(full_response)
#                     spinner.__exit__(None, None, None)
#                 except StopIteration:
#                     spinner.__exit__(None, None, None)
#                     st.warning("No response received.")

#                 for chunk in stream:
#                     full_response += chunk
#                     message_placeholder.markdown(full_response)

#             st.session_state.messages.append({"role": "assistant", "content": full_response})

#             if sources:
#                 with st.expander("📚 Source Texts Used"):
#                     st.markdown(sources.replace("\\n", "\n"))

#         except Exception as e:
#             st.error(f"❌ Streaming failed: {e}")


# import streamlit as st
# import requests
# import logging
# import time
# from typing import Generator

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Constants
# API_URL = "http://localhost:8000/api/generate"

# st.set_page_config(page_title="AI Job Generator", layout="centered")
# st.title("🛠️ Job Description Generator")

# # Input Fields
# model = st.text_input("Model", value="gemma:2b")
# prompt = st.text_area("Prompt", value="Can you build a basic program of Android?")
# stream = False

# if st.button("Generate"):
#     payload = {
#         "model": model,
#         "prompt": prompt,
#         "stream": stream
#     }

#     try:
#         with st.spinner("Fetching response..."):
#             logger.info(f"Request sent to {API_URL} with payload: {payload}")

#             response = requests.post(API_URL, json=payload)
#             logger.info(f"Response received: {response.status_code} - {response.text}")
#             # response.raise_for_status()
#             data = response.json()

#         # Display result
#         st.subheader("📄 Response")
#         st.code(response.text)

#     except requests.exceptions.RequestException as e:
#         st.error(f"Request failed: {e}")


# def stream_answer() -> Generator[str, None, None]:
#     for word in response.text.split():  # You can split by char for finer tokens
#         yield word + " "
#         time.sleep(0.05)

#     return (stream_answer(), media_type="text/plain")

import streamlit as st
import requests
import time


# Your API (which wraps Ollama and returns plain text)
MY_API_URL = "http://justjobglobal.in:8080/api/generate"  # or wherever it's hosted

st.set_page_config(page_title="🧠 Chat Bot", layout="centered")
st.title("💬 Hello, I am a Chat Bot!")

with st.sidebar:
    selected_model = st.selectbox("Model", ["mistral", "gemma:2b", "gpt-oss"])
    speed = st.slider("Typing Speed (sec per word)", 0.01, 0.2, 0.05)

prompt = st.text_area("📝 Ask Anything:")

if st.button("🚀 Generate"):
    if not prompt.strip():
        st.warning("Please enter a ask anything.")
    else:
        with st.spinner("Thinking..."):
            payload = {
                "model": selected_model,
                "prompt": prompt,
                "stream": False  # Your backend handles this
            }

            try:
                response = requests.post(MY_API_URL, json=payload, timeout=6000)
                response.raise_for_status()

                # result = response.json()
                # result_text = result.get("response", "") # ✅ Plain text response
                result_text = response.text  # ✅ Plain text response

                # Stream simulation
                placeholder = st.empty()
                streamed = ""

                for word in result_text.split():
                    streamed += word + " "
                    placeholder.markdown(streamed + "▌")
                    time.sleep(speed)

                placeholder.markdown(streamed)

            except Exception as e:
                st.error(f"Oops.... Server might be down or the request took too long.")
