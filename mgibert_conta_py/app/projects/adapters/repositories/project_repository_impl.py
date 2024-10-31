import uuid
from typing import List, Union, Type

from sqlalchemy.orm import Session

from mgibert_conta_py.app.projects.adapters.database.models.project_model import ProjectModel
from mgibert_conta_py.app.projects.domain.entities.project import Project
from mgibert_conta_py.app.projects.domain.repositories.project_repository import ProjectRepository


class ProjectRepositoryImpl(ProjectRepository):

    def __init__(self, storage: Session):
        self.storage: Session = storage

    def save(self, project: Project) -> Project:
        db_project = ProjectModel(project_id=project.project_id,
                                  key=project.key,
                                  description=project.description,
                                  period=project.period)
        self.storage.add(db_project)
        self.storage.commit()
        self.storage.refresh(db_project)
        return self.serialize(db_project)


    def get(self, project_id: uuid.UUID) -> Project:
        db_project = self.storage.query(ProjectModel).get(project_id)
        return self.serialize(db_project)

    def get_all(self) -> List[Project]:
        db_project_list = self.storage.query(ProjectModel).all()
        return [self.serialize(db_project) for db_project in db_project_list]

    @staticmethod
    def serialize(db_project: Union[ProjectModel, Type[ProjectModel]]) -> Project:
        return Project(project_id=db_project.project_id,
                       key=db_project.key,
                       description=db_project.description,
                       period=db_project.period)
