import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import status
from starlette.responses import JSONResponse

from mgibert_conta_py.app.database import get_session
from mgibert_conta_py.app.periods.adapters.external.period_service_impl import PeriodFinderImpl
from mgibert_conta_py.app.projects.adapters.repositories.project_repository_impl import ProjectRepositoryImpl
from mgibert_conta_py.app.projects.application.project_create import ProjectCreateService
from mgibert_conta_py.app.projects.domain.entities.project import Project

router = APIRouter()

@router.post('/projects', status_code=status.HTTP_201_CREATED)
def create_project(project: Project, storage: Session = Depends(get_session)):
    repository = ProjectRepositoryImpl(storage)
    period_finder = PeriodFinderImpl(storage)
    service = ProjectCreateService(repository, period_finder)
    result = service.create_project(project)
    return result

@router.get('/projects')
def get_all_projects(storage: Session = Depends(get_session)):
    pass
    # repository = PeriodRepositoryImpl(storage)
    # service = PeriodService(repository)
    # result = service.get_all_periods()
    # return result

@router.get('/projects/{project_id}')
def get_project(project_id: uuid.UUID, storage: Session = Depends(get_session)):
    pass
