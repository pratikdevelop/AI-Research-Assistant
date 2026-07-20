from langchain_chroma import Chroma

from rag.embeddings import get_embeddings
from storage.storage_manager import StorageManager


class ChromaDBManager:

    def __init__(self, project_id):

        self.project_id = project_id

        self.embeddings = get_embeddings()

        self.persist_directory = (
            StorageManager.get_chroma_directory(
                project_id
            )
        )

    # --------------------------------------

    def load_vector_store(self):

        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings,
        )

    # --------------------------------------

    def add_documents(self, documents):

        vector_store = self.load_vector_store()

        vector_store.add_documents(documents)

        return vector_store

    # --------------------------------------

    def similarity_search(
        self,
        query,
        k=4,
    ):

        vector_store = self.load_vector_store()

        return vector_store.similarity_search(
            query=query,
            k=k,
        )

    # --------------------------------------

    def delete_collection(self):

        vector_store = self.load_vector_store()

        vector_store.delete_collection()