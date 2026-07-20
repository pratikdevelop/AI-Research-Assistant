from database.chromadb_manager import ChromaDBManager


def retrieve_documents(
    project_id: str,
    query: str,
    k: int = 4,
):
    """
    Retrieve the most relevant documents from the project's ChromaDB.
    """

    manager = ChromaDBManager(project_id)

    return manager.similarity_search(
        query=query,
        k=k,
    )


# --------------------------------------------------


def format_documents(docs):
    """
    Format retrieved documents before sending them to the LLM.
    Includes metadata for proper source attribution.
    """

    if not docs:
        return "No relevant information found."

    formatted_docs = []

    for doc in docs:

        metadata = doc.metadata or {}

        source = metadata.get("source", "Unknown")

        filename = metadata.get("filename", "Unknown")

        page = metadata.get("page", "N/A")

        formatted_docs.append(
            f"""
Source: {source}
Filename: {filename}
Page: {page}

Content:
{doc.page_content}
"""
        )

    return "\n\n------------------------------\n\n".join(
        formatted_docs
    )