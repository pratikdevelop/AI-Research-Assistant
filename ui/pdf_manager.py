import os
import streamlit as st
from storage.storage_manager import StorageManager
from rag.loader import load_pdf
from rag.splitter import split_documents
from rag.vectorstore import create_vector_store


def process_pdf(uploaded_pdf):

    if uploaded_pdf is None:
        return

    os.makedirs("uploads", exist_ok=True)


    pdf_dir = StorageManager.get_pdf_directory(
        project_id
    )

    pdf_path = os.path.join(
        pdf_dir,
        uploaded_pdf.name,
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    with st.spinner("📖 Processing PDF..."):

        documents = load_pdf(pdf_path)

        chunks = split_documents(documents)

        create_vector_store(chunks)
        st.success("✅ ChromaDB Vector Store Created!")


    st.success("✅ PDF processed successfully!")

    with st.expander("📊 PDF Statistics"):

        st.write(f"Pages : {len(documents)}")

        st.write(f"Chunks : {len(chunks)}")

        st.write("Database : ChromaDB")