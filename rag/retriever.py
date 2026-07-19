# # # def get_retriever(vector_store):

# # #     return vector_store.as_retriever(
# # #         search_kwargs={
# # #             "k": 4
# # #         }
# # #     )
    
# # # def retrieve_documents(vector_store, query):

# # #     docs = vector_store.similarity_search(
# # #         query,
# # #         k=3,
# # #     )

# # #     return docs


# # from database.chromadb_manager import ChromaDBManager


# # def retrieve_documents(
# #     query,
# #     k=3,
# # ):

# #     manager = ChromaDBManager()

# #     return manager.similarity_search(
# #         query,
# #         k,
# #     )


# from langchain_chroma import Chroma

# from rag.embeddings import get_embeddings


# def retrieve_documents(query: str, k: int = 4):

#     vector_store = Chroma(
#         persist_directory="chroma_db",
#         embedding_function=get_embeddings(),
#     )

#     docs = vector_store.similarity_search(
#         query,
#         k=k,
#     )

#     return docs


from database.chromadb_manager import ChromaDBManager


def retrieve_documents(
    project_id,
    query,
    k=4,
):

    manager = ChromaDBManager(project_id)

    return manager.similarity_search(
        query=query,
        k=k,
    )