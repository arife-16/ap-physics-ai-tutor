import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# --- CONFIGURATION & LOADING ---
load_dotenv()

# Function to load the vector database
@st.cache_resource
def load_vector_store():
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    except Exception as e:
        st.error(f"Failed to load the knowledge base. Please run ingest.py first. Error: {e}")
        return None

# Load the FAISS index
vector_store = load_vector_store()
if vector_store is None:
    st.stop() 

# Initialize Groq client
try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
except Exception as e:
    st.error("Could not initialize the Groq API client. Check your GROQ_API_KEY.")
    st.stop()

# --- UI SETUP---
st.set_page_config(page_title="AP Physics C AI Tutor", page_icon="⚛️", layout="wide")

st.title("⚛️ AP Physics C AI Tutor")
st.subheader("Your personal guide for mastering AP Physics C: Mechanics")
st.markdown("---")

# --- RAG-ENABLED CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! How can I help you with AP Physics C today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about Kinematics, Newton's Laws, etc..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        # 1. RETRIEVE CONTEXT
        retrieved_docs = vector_store.similarity_search(prompt, k=3)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # 2. AUGMENT THE PROMPT
        rag_prompt = f"""
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
        $$K = \\frac{{1}}{{2}}mv^2$$
        Does that formula look familiar to you?"
        ### END OF EXAMPLE ###

        Now, begin the conversation with the student.

        use a Socratic, Chain-of-Thought method.

        You must use LaTeX for all math.

        CONTEXT:
        ---
        {context}
        ---

        USER'S QUESTION:
        {prompt}
        """

        # 3. GENERATE RESPONSE
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": rag_prompt}],
                model="llama3-8b-8192",
            )
            response = chat_completion.choices[0].message.content
            
            with st.chat_message("assistant"):
                st.markdown(response)
            
            st.session_state.messages.append({"role": "assistant", "content": response})

        except Exception as e:
            st.error(f"An error occurred: {e}")