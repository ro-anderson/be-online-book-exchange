from typing import Dict, List, Type
from src.data.interfaces import DonationRepositorySpy as DonationRepositorySpy
from src.domain.use_cases import FindDonation as FindDonationInterface
from src.domain.models import Donations


class FindDonation(FindDonationInterface):
    """ Class to define usecase: Find Donation """

    def __init__(self, donation_repository: Type[DonationRepositorySpy]):
        self.donation_repository = donation_repository

    def by_donation_id(self, donation_id: int) -> Dict[bool, List[Donations]]:
        """Select Donation By donation_id
        :param - donation_id: id of the donation
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(donation_id, int)

        if validate_entry:
            response = self.donation_repository.select_donation(donation_id=donation_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Donations]]:
        """Select Donation By user_id
        :param - user_id: id of the user owne of the donation
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.donation_repository.select_donation(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_donation_id_and_user_id(
        self, donation_id: int, user_id: int
    ) -> Dict[bool, List[Donations]]:
        """Select Donation By user_id
        :param - user_id: id of the user owne of the donation
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(donation_id, int)

        if validate_entry:
            response = self.donation_repository.select_donation(donation_id=donation_id, user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_donation_name(
        self, name: str
    ) -> Dict[bool, List[Donations]]:
        """Select Donation By user_id
        :param - user_id: id of the user owne of the donation
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.donation_repository.select_donation(name=name)

        return {"Success": validate_entry, "Data": response}
