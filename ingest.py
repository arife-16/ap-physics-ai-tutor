import os
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# --- Configuration ---
# Make sure this points to your file
SOURCE_FILE_PATH = "AP-Physics-C-Mech.pdf" 
FAISS_INDEX_PATH = "faiss_index"

def main():
    """
    Main function to ingest document, split it, create embeddings,
    and save them to a FAISS vector store.
    """
    print("Starting document ingestion process...")

    # 1. Load the document
    if not os.path.exists(SOURCE_FILE_PATH):
        print(f"Error: Source file not found at '{SOURCE_FILE_PATH}'")
        return
        
    loader = UnstructuredFileLoader(SOURCE_FILE_PATH)
    documents = loader.load()
    print(f"Loaded {len(documents)} document(s).")

    # 2. Split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    print(f"Split document into {len(chunks)} chunks.")

    # --- DEBUG STEP 2: CHECK CHUNKS ---
    # If chunks were created, this will stop the script before the error.
    if not chunks:
        print("!!! Error: Failed to split document into chunks. Please check the document content and splitter settings.")
        return

    # 3. Create embeddings and FAISS vector store
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        print("Embedding model loaded.")
        vector_store = FAISS.from_documents(chunks, embeddings)
        print("FAISS vector store created.")
        vector_store.save_local(FAISS_INDEX_PATH)
        print(f"Vector store saved to '{FAISS_INDEX_PATH}'")
    except Exception as e:
        print(f"An error occurred during embedding or FAISS creation: {e}")
        # This will print the full traceback for the error
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # Make sure you have your GOOGLE_API_KEY set as an environment variable
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set.")
    else:
        main()