from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Donations


class DonationRepositorySpy(ABC):
    """ Interface to Donation Repository """

    @abstractmethod
    def insert_donation(self, name: str, category: str, user_id: int) -> Donations:
        """ abstractmethod  """

        raise Exception("Method not implemented")

    @abstractmethod
    def select_donation(self, donation_id: int = None, user_id: int = None) -> List[Donations]:
        """ abstractmethod  """

        raise Exception("Method not implemented")
