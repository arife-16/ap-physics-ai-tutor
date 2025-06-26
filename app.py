# app.py - FINAL, ROBUST VERSION

import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# --- CONFIGURATION & API KEY (Robust Version) ---
# Create an explicit path to the .env file in the same directory as the script
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

# Load the .env file from the specified path
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)
    st.success("Successfully loaded the .env file.")
else:
    st.error(".env file not found. Please ensure it is in the same directory as app.py.")
    st.stop()


# Now, try to initialize the Groq client
try:
    # Use os.getenv to read the key that was just loaded
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in the .env file.")
    
    client = Groq(api_key=groq_api_key)
    st.success("Groq API client initialized successfully!")

except Exception as e:
    st.error(f"Could not initialize the Groq API client: {e}")
    st.stop()


# --- UI & SIDEBAR (No changes needed here) ---
with st.sidebar:
    st.header("About EduBeyond")
    st.info(
        "EduBeyond is an AI-powered tutor designed to help you master the concepts of "
        "AP Physics C: Mechanics and Electricity & Magnetism."
    )
    # ... (the rest of your sidebar code)

st.title("AP Physics C AI Tutor")
st.markdown("Welcome to your personal physics assistant, **EduBeyond**! How can I help you prepare today?")


# --- SYSTEM PROMPT ---
# Use the full "Few-Shot CoT" system prompt that we created before
system_prompt = """
You are an expert AP Physics C tutor named EduBeyond. Your primary directive is to use Chain-of-Thought reasoning to guide students to their own conclusions.

### RULES ###
1.  **Guide, Don't Solve:** Each step in your thought process must end with a guiding question.
2.  **Forceful LaTeX Formatting:** Every step of your reasoning must use proper LaTeX for all mathematics. This is not optional. Use single dollar signs for inline math (e.g., `$v_i$`) and double dollar signs for equations (e.g., `$$F=ma$$`).
3.  **Use Precise Terminology:** Your explanations must use terminology appropriate for the AP Physics C curriculum.
4.  **Maintain Conversational Pacing:** Generate only one step and one question at a time.
5.  **Acknowledge and Reinforce:** When a student is correct, use positive reinforcement.

### PERFECT EXAMPLE CONVERSATION ###
Student: "Hi, what's the formula for kinetic energy?"

EduBeyond: "Great question! The formula for kinetic energy, `$K$`, depends on an object's mass, `$m$`, and its velocity, `$v$`. The equation is:
$$K = \frac{1}{2}mv^2$$
Does that formula look familiar to you?"
### END OF EXAMPLE ###

Now, begin the conversation with the student.
"""

# --- CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm EduBeyond, your AP Physics C Tutor. How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about AP Physics C..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    api_messages = [{"role": "system", "content": system_prompt}] + st.session_state.messages

    with st.spinner("EduBeyond is thinking..."):
        try:
            chat_completion = client.chat.completions.create(
                messages=api_messages,
                model="llama3-8b-8192",
            )
            response = chat_completion.choices[0].message.content
            
            with st.chat_message("assistant"):
                st.markdown(response)
            
            st.session_state.messages.append({"role": "assistant", "content": response})

        except Exception as e:
            st.error(f"An error occurred with the Groq API: {e}")