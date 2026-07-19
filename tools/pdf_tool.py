from langchain.tools import tool

from rag.retriever import retrieve_documents


@tool
def pdf_search(query: str) -> str:
    """
    Search the uploaded PDF for relevant information.
    """

    docs = retrieve_documents(query)

    if not docs:
        return "No relevant information found in the uploaded PDF."

    context = []

    for doc in docs:

        context.append(doc.page_content)

    return "\n\n".join(context)