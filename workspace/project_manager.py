from database.mongodb import MongoDBManager


class ProjectManager:

    def __init__(self):

        self.db = MongoDBManager()

    def create_project(

        self,

        name,

        description="",

    ):

        return self.db.create_project(

            name,

            description,

        )

    def get_projects(self):

        return self.db.get_projects()

    def add_pdf(

        self,

        project_name,

        filename,

    ):

        self.db.add_pdf(

            project_name,

            filename,

        )