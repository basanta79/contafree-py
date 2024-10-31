import uuid
from abc import ABC, abstractmethod
from typing import List

from mgibert_conta_py.app.projects.domain.entities.project import Project


class ProjectRepository(ABC):

    @abstractmethod
    def save(self, project: Project) -> Project:
        raise NotImplementedError

    @abstractmethod
    def get(self, project_id: uuid.UUID) -> Project:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Project]:
        raise NotImplementedError
