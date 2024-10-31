from mgibert_conta_py.app.projects.domain.repositories.project_repository import ProjectRepository


class ProjectGetService:

    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def get_project_by_period(self, period: str):
