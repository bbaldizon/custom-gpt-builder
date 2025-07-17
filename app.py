import streamlit as st
import openai
import os

# Set your OpenAI API key securely in Streamlit Cloud
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Custom GPT Builder", layout="centered")
st.title("🛠️ Custom GPT Builder")
st.markdown("""
Let’s design a custom GPT together! Whether it’s for tasks, coaching, or creative work, we’ll walk through the key decisions step-by-step.
""")

# Identity collection
with st.sidebar:
    st.header("User Info")
    user_name = st.text_input("Your name")
    user_email = st.text_input("Your district email")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": """You are a warm, curious, and helpful assistant that supports educators and school staff in building their own custom GPTs. Guide users step-by-step. Start by asking if they want to build a task-specific GPT (e.g., for writing or organizing), a thought-partner GPT (for reflection or brainstorming), or another kind. Once they choose, help them clarify:

- What the GPT should do
- What kinds of input they will give it
- What great outputs look like
- How it should sound and behave
- Any examples or patterns it should learn from

Help the user generate draft instructions they can paste into a GPT’s instruction field. Avoid jargon. Be friendly, supportive, and non-technical."""}
    ]

# Chat interface
user_input = st.chat_input("What kind of GPT do you want to create?")
if user_input:
    user_identity = f"User: {user_name}, Email: {user_email}"
    st.session_state.messages.append({"role": "user", "content": user_identity + "\n\n" + user_input})

    with st.spinner("Helping you design your GPT..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.messages,
            temperature=0.7,
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})

# Display chat history
for msg in st.session_state.messages[1:]:  # Skip system prompt in display
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
