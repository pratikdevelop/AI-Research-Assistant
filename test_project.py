from workspace.project_manager import ProjectManager

pm = ProjectManager()

project_id = pm.create_project(

    "AI Agents",

    "Research about AI agents"

)

print(project_id)

print()

print(pm.get_projects())