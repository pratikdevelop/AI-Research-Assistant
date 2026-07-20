import os
import streamlit as st

from storage.storage_manager import StorageManager
from database.chromadb_manager import ChromaDBManager

from rag.loader import load_pdf
from rag.splitter import split_documents
from database.mongodb import MongoDBManager

db = MongoDBManager()

def process_pdf(uploaded_pdf, project_id):

    if uploaded_pdf is None:
        return
    
    
  
    if db.pdf_exists(
        project_id,
        uploaded_pdf.name,
    ):
        st.warning("⚠️ This PDF has already been uploaded.")
        return

    pdf_dir = StorageManager.get_pdf_directory(project_id)

    pdf_path = os.path.join(
        pdf_dir,
        uploaded_pdf.name,
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.getbuffer())

    with st.spinner("📖 Processing PDF..."):

        documents = load_pdf(pdf_path)

        chunks = split_documents(documents)
        for chunk in chunks:

            chunk.metadata.update(
                {
                    "project_id": project_id,
                    "filename": uploaded_pdf.name,
                    "source": "PDF",
                }
            )

        chroma = ChromaDBManager(project_id)

        chroma.add_documents(chunks)
        db.save_pdf(
            project_id=project_id,
            filename=uploaded_pdf.name,
            pages=len(documents),
            chunks=len(chunks),
            file_size=uploaded_pdf.size,
        )

        st.success("✅ ChromaDB Vector Store Created!")

    st.success("✅ PDF processed successfully!")

    with st.expander("📊 PDF Statistics"):

        st.write(f"Pages : {len(documents)}")
        st.write(f"Chunks : {len(chunks)}")
        st.write("Embedding Model : all-MiniLM-L6-v2")
        st.write("Vector Database : ChromaDB")