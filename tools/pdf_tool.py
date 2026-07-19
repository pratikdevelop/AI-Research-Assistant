# from langchain.tools import tool

# from rag.retriever import retrieve_documents


# @tool
# def pdf_search(query: str) -> str:
#     """
#     Search the uploaded PDF for relevant information.
#     """

#     docs = retrieve_documents(
#     project_id,
#     query,
# )

#     if not docs:
#         return "No relevant information found in the uploaded PDF."

#     context = []

#     for doc in docs:

#         context.append(doc.page_content)

#     return "\n\n".join(context)



from langchain.tools import Tool

from rag.retriever import retrieve_documents


def get_pdf_tool(project_id):

    def pdf_search(query):

        docs = retrieve_documents(
            project_id,
            query,
        )

        if not docs:
            return "No relevant information."

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    return Tool.from_function(
        func=pdf_search,
        name="PDF Search",
        description="Search uploaded PDFs."
    )