from abc import ABC, abstractmethod

from mgibert_conta_py.app.periods.domain.entities.period import Period


class PeriodFinder(ABC):

    @abstractmethod
    def find_by_name(self, name: str) -> Period:
        pass
