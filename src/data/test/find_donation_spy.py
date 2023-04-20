from typing import Dict, List
from src.domain.models import Donations
from src.domain.test import mock_donation


class FindDonationSpy:
    """ Class to mock usecase: Find Donation """

    def __init__(self, donation_repository: any):
        self.donation_repository = donation_repository
        self.by_donation_id_param = {}
        self.by_user_id_param = {}
        self.by_donation_id_and_user_id_param = {}

    def by_donation_id(self, donation_id: int) -> Dict[bool, List[Donations]]:
        """ Select Donation By donation_id """

        self.by_donation_id_param["donation_id"] = donation_id
        response = None
        validate_entry = isinstance(donation_id, int)

        if validate_entry:
            response = [mock_donation()]

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Donations]]:
        """ Select Donation By user_id """

        self.by_user_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_donation()]

        return {"Success": validate_entry, "Data": response}

    def by_donation_id_and_user_id(
        self, donation_id: int, user_id: int
    ) -> Dict[bool, List[Donations]]:
        """ Select Donation By user_id """

        self.by_donation_id_and_user_id_param["donation_id"] = donation_id
        self.by_donation_id_and_user_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int) and isinstance(donation_id, int)

        if validate_entry:
            response = [mock_donation()]

        return {"Success": validate_entry, "Data": response}
