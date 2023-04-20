from typing import List
from src.domain.models import Donations
from src.domain.test import mock_donation


class DonationRepositorySpy:
    """ Spy to Donation Repository """

    def __init__(self):
        self.insert_donation_param = {}
        self.select_donation_param = {}

    def insert_donation(self, name: str, category: str, user_id: int) -> Donations:
        """ Spy all the attributes """

        self.insert_donation_param["name"] = name
        self.insert_donation_param["category"] = category
        self.insert_donation_param["user_id"] = user_id

        return mock_donation()

    def select_donation(self, donation_id: int = None, user_id: int = None) -> List[Donations]:
        """ Spy all the attributes """

        self.select_donation_param["donation_id"] = donation_id
        self.select_donation_param["user_id"] = user_id

        return [mock_donation()]
