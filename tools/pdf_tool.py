from langchain_core.tools import tool

from rag.retriever import (
    retrieve_documents,
    format_documents,
)


def get_pdf_tool(project_id):
    """
    Create a PDF search tool for a specific project.
    """

    @tool
    def pdf_search(query: str) -> str:
        """
        Search the uploaded PDFs for relevant information.
        """

        docs = retrieve_documents(
            project_id=project_id,
            query=query,
        )

        if not docs:
            return "No relevant information found in the uploaded PDFs."

        return format_documents(docs)

    return pdf_search