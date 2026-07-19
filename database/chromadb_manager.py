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

    def create_vector_store(self, documents):

        return Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.persist_directory,
        )

    def load_vector_store(self):

        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings,
        )

    def similarity_search(
        self,
        query,
        k=4,
    ):

        return self.load_vector_store().similarity_search(
            query=query,
            k=k,
        )