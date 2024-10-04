from abc import ABC, abstractmethod
from typing import List

from mgibert_conta_py.app.periods.domain.entities.period import Period


class PeriodRepository(ABC):

    @abstractmethod
    def save(self, period: Period) -> Period:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Period]:
        raise NotImplementedError
