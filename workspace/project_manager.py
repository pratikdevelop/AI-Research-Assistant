from database.mongodb import MongoDBManager


class ProjectManager:

    def __init__(self):
        self.db = MongoDBManager()

    def create_project(self, name, description=""):
        return self.db.create_project(name, description)

    def get_projects(self):
        return self.db.get_projects()

    def get_project(self, project_id):
        return self.db.get_project(project_id)

    def get_project_names(self):
        projects = self.get_projects()

        return [project["project_name"] for project in projects]

    # def get_project_by_name(self, project_name)
    def get_project_by_name(self, project_name):
        return self.db.get_project_by_name(project_name)