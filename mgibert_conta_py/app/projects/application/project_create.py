from sys import exception
from uuid import uuid4

from mgibert_conta_py.app.periods.domain.period_finder import PeriodFinder
from mgibert_conta_py.app.projects.domain.entities.project import Project
from mgibert_conta_py.app.projects.domain.repositories.project_repository import ProjectRepository


class ProjectCreateService:

    def __init__(self, project_repository: ProjectRepository, period_finder: PeriodFinder):
        self.project_repository = project_repository
        self.period_finder = period_finder

    def create_project(self, project: Project) -> Project:
        project.project_id = uuid4()
        period = self._ensure_period_exists(project.period)
        if period is None:
            raise Exception()
        stored_project = self.project_repository.save(project)
        return stored_project


    def _ensure_period_exists(self, name: str):
        return self.period_finder.find_by_name(name)
