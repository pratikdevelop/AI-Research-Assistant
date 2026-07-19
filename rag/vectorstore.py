from database.chromadb_manager import ChromaDBManager


def create_vector_store(documents):

    manager = ChromaDBManager()

    return manager.create_vector_store(documents)