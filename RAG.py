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
st.set_page_config(
    page_title="AP Physics C AI Tutor",
    page_icon="⚛️",
    layout="centered" 
)


with st.sidebar:
    st.header("About EduBeyond")
    st.info(
        "EduBeyond is an AI-powered tutor designed to help you master the concepts of "
        "AP Physics C: Mechanics and Electricity & Magnetism. Ask it conceptual questions, "
        "calculation problems, or for help with derivations."
    )
    
    st.header("Key Constants")
    # Using an expander to keep the sidebar tidy
    with st.expander("Show Physics Constants"):
        st.latex("g = 9.8 \\, \\text{m/s}^2")
        st.latex("k = 8.99 \\times 10^9 \\, \\text{N} \\cdot \\text{m}^2/\\text{C}^2")
        st.latex("\\epsilon_0 = 8.85 \\times 10^{-12} \\, \\text{C}^2/(\\text{N} \\cdot \\text{m}^2)")
        st.latex("\\mu_0 = 4\\pi \\times 10^{-7} \\, (\\text{T} \\cdot \\text{m})/\\text{A}")

st.title("⚛️ AP Physics C AI Tutor")
st.markdown("Welcome to your personal physics assistant, **EduBeyond**! How can I help you prepare today?")
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

    with st.spinner("EduBeyond is thinking..."):
        # 1. RETRIEVE CONTEXT
        retrieved_docs = vector_store.similarity_search(prompt, k=3)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # 2. AUGMENT THE PROMPT
        rag_prompt = f"""
        You are an expert AP Physics C tutor for high school students. Your name is EduBeyond.
        Your tone is encouraging, clear, and professional. Your primary directive is to use Chain-of-Thought reasoning to guide students to their own conclusions.

        ### RULES ###
        1.  **Start with formal definition:** Start with formal definition of the topic the student asks you about and the area of usage of that topic.
        2.  **Guide, Don't Solve:** Each step in your thought process must end with a guiding question.
        3.  **Step-by-Step Reasoning:** For any calculation, derivation, or complex problem, you MUST break down your reasoning into a logical, step-by-step process. Explain the "why" behind each step.
        4.  **Forceful LaTeX Formatting:** Every step of your reasoning must use proper LaTeX for all mathematics and render it inside the chat.
        5.  **Use AP Physics C Terminology:** Use terms like 'integral', 'derivative', 'moment of inertia', 'Gauss's Law', etc., where appropriate.
        6.  **Check for Understanding:** After a complex explanation, ask a follow-up question.
        7.  **Maintain Conversational Pacing:** Generate only one step and one question at a time.
        8.  **Acknowledge and Reinforce:** When a student is correct, use positive reinforcement.

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