import os


class StorageManager:

    BASE_DIR = "storage"

    @classmethod
    def get_project_directory(cls, project_id):

        path = os.path.join(
            cls.BASE_DIR,
            project_id,
        )

        os.makedirs(path, exist_ok=True)

        return path

    @classmethod
    def get_chroma_directory(cls, project_id):

        path = os.path.join(
            cls.get_project_directory(project_id),
            "chroma_db",
        )

        os.makedirs(path, exist_ok=True)

        return path

    @classmethod
    def get_pdf_directory(cls, project_id):

        path = os.path.join(
            cls.get_project_directory(project_id),
            "pdfs",
        )

        os.makedirs(path, exist_ok=True)

        return path