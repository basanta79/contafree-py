import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import status

from mgibert_conta_py.app.database import get_session
from mgibert_conta_py.app.periods.domain.entities.period import Period

router = APIRouter()

@router.post('/projects', status_code=status.HTTP_201_CREATED)
def create_project(project: Period, storage: Session = Depends(get_session)):
    pass
    # repository = PeriodRepositoryImpl(storage)
    # service = PeriodService(repository)
    # result = service.create_period(period)
    # return result
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)

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
