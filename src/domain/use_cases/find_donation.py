from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Donations


class FindDonation(ABC):
    """ Interface to FindDonation use case """

    @abstractmethod
    def by_donation_id(self, donation_id: int) -> Dict[bool, List[Donations]]:
        """ Specific case """

        raise Exception("Should implement method: by_donation_id")

    @abstractmethod
    def by_user_id(self, user_id: int) -> Dict[bool, List[Donations]]:
        """ Specific case """

        raise Exception("Should implement method: by_user_id")

    @abstractmethod
    def by_donation_id_and_user_id(
        self, donation_id: int, user_id: int
    ) -> Dict[bool, List[Donations]]:
        """ Specific case """

        raise Exception("Should implement method: by_donation_id_and_user_id")

    @abstractmethod
    def by_donation_name(self, name: str) -> Dict[bool, List[Donations]]:
        """ Specific case """

        raise Exception("Should implement method: by_donation_id")
