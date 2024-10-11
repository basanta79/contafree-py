import pytest
from sqlalchemy.orm import Session

from mgibert_conta_py.app.periods.adapters.database.models.period_model import PeriodModel
from mgibert_conta_py.app.periods.adapters.repositories.period_repository_impl import PeriodRepositoryImpl
from mgibert_conta_py.app.periods.application.period_service import PeriodService
from mgibert_conta_py.app.periods.domain.entities.period import Period
from mgibert_conta_py.test.integration_test import storage


def test_create_period(storage: Session):

    # Given
    new_period = Period(
        period_id=None,
        period_name="01-02"
    )
    period_repository = PeriodRepositoryImpl(storage)

    # When
    service = PeriodService(period_repository)
    sut = service.create_period(new_period)

    saved_period = storage.query(PeriodModel) .filter_by(period_id=sut.period_id).first()

    assert saved_period is not None
    assert saved_period.period_name == "01-02"
    assert sut.period_id == saved_period.period_id
