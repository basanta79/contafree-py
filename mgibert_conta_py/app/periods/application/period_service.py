from typing import List
from uuid import uuid4

from mgibert_conta_py.app.periods.domain.entities.period import Period
from mgibert_conta_py.app.periods.domain.repositories.period_repository import PeriodRepository


class PeriodService:

    def __init__(self, period_repository: PeriodRepository):
        self.period_repository = period_repository

    def create_period(self, period: Period) -> Period:
        period.period_id = uuid4()
        stored_period = self.period_repository.save(period)
        return stored_period

    def get_all_periods(self) -> List[Period]:
        return self.period_repository.get_all()
