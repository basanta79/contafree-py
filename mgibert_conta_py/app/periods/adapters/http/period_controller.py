from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import status

from mgibert_conta_py.app.database import get_session
from mgibert_conta_py.app.periods.adapters.repositories.period_repository_impl import PeriodRepositoryImpl
from mgibert_conta_py.app.periods.application.period_service import PeriodService
from mgibert_conta_py.app.periods.domain.entities.period import Period

router = APIRouter()

@router.post('/periods', status_code=status.HTTP_201_CREATED)
def create_period(period: Period, storage: Session = Depends(get_session)):
    repository = PeriodRepositoryImpl(storage)
    service = PeriodService(repository)
    result = service.create_period(period)
    return result
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)

@router.get('/periods')
def get_all_periods(storage: Session = Depends(get_session)):
    repository = PeriodRepositoryImpl(storage)
    service = PeriodService(repository)
    result = service.get_all_periods()
    return result
