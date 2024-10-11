from typing import List

from sqlalchemy.orm import Session

from mgibert_conta_py.app.periods.adapters.database.models.period_model import PeriodModel
from mgibert_conta_py.app.periods.domain.entities.period import Period
from mgibert_conta_py.app.periods.domain.repositories.period_repository import PeriodRepository


class PeriodRepositoryImpl(PeriodRepository):

    def __init__(self, storage: Session):
        self.storage: Session = storage

    def save(self, period: Period) -> Period:
        db_period = PeriodModel(period_name=period.period_name)
        self.storage.add(db_period)
        self.storage.commit()
        self.storage.refresh(db_period)  # Actualizar el objeto con los datos almacenados en la DB
        return Period(
            period_id=db_period.period_id,
            period_name=db_period.period_name,
        )

    def get_all(self) -> List[Period]:
        return self.storage.query(PeriodModel).all()
