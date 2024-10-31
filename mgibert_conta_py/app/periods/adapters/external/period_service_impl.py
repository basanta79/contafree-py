from sqlalchemy.orm import Session

from mgibert_conta_py.app.periods.adapters.repositories.period_repository_impl import PeriodRepositoryImpl
from mgibert_conta_py.app.periods.application.period_service import PeriodService
from mgibert_conta_py.app.periods.domain.entities.period import Period
from mgibert_conta_py.app.periods.domain.period_finder import PeriodFinder


class PeriodFinderImpl(PeriodFinder):

    def __init__(self, storage: Session):
        self.storage: Session = storage

    def find_by_name(self, name: str) -> Period:
        repository = PeriodRepositoryImpl(self.storage)
        period_service = PeriodService(repository)
        period = period_service.find_by_name(name)
        return period
