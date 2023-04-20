from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import Donations


class RegisterDonation(ABC):
    """ Interface to FindDonation use case """

    @abstractclassmethod
    def registry(
        cls, name: str, category: str, user_information: Dict[int, str]
    ) -> Dict[bool, Donations]:
        """ use case """

        raise Exception("Should implement method: registry")
