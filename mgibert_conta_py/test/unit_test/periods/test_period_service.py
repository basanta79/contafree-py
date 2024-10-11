from unittest.mock import MagicMock

import pytest

from mgibert_conta_py.app.periods.application.period_service import PeriodService
from mgibert_conta_py.app.periods.domain.entities.period import Period


@pytest.fixture
def period_repository():
    return MagicMock()


def test_when_create_period_should_return_period_with_uuid_created(period_repository):

    # Given
    new_period = Period(
        period_id=None,
        period_name="23-24"
    )
    period_repository.save.return_value = new_period

    # When
    service = PeriodService(period_repository)
    sut = service.create_period(new_period)

    # Then
    period_repository.save.assert_called_once()
    assert sut.period_id is not None
    assert sut.period_name == "23-24"

def test_when_get_all_periods_should_return_list_of_periods(period_repository):

    # Given
    period = Period(
        period_id="123e4567-e89b-12d3-a456-426614174002",
        period_name="23-24"
    )
    period_repository.get_all.return_value = [period]

    # When
    service = PeriodService(period_repository)
    sut = service.get_all_periods()

    # Then
    isinstance(sut, list)
    isinstance(sut[0], Period)
