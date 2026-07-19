from langchain_chroma import Chroma

from rag.embeddings import get_embeddings


class ChromaDBManager:

    def __init__(self):

        self.embeddings = get_embeddings()

        self.persist_directory = "chroma_db"

    def create_vector_store(self, documents):

        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.persist_directory,
        )

        return vector_store

    def load_vector_store(self):

        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeddings,
        )

    def similarity_search(
        self,
        query,
        k=3,
    ):

        vector_store = self.load_vector_store()

        return vector_store.similarity_search(
            query=query,
            k=k,
        )