from typing import Type, Dict, List
from src.data.find_user import FindUser
from src.data.interfaces import DonationRepositorySpy as DonationRepositorySpy
from src.domain.use_cases import RegisterDonation as RegisterDonationInterface
from src.domain.models import Users, Donations


class RegisterDonation(RegisterDonationInterface):
    """ Class to define use case: Register Donation """

    def __init__(self, donation_repository: [DonationRepositorySpy], find_user: Type[FindUser]):
        self.donation_repository = donation_repository
        self.find_user = find_user

    def registry(
        self, name: str, category: str, user_information: Dict[int, str],
    ) -> Dict[bool, Donations]:
        """Registry Donation
        :param - name: donation name
               - category: type of the category
               - user_information: Dictionaty with user_id and/or user_name
        :return - Dictionaty with informations of the process
        """

        response = None

        # Validating entry and trying to find an user
        validate_entry = isinstance(name, str) and isinstance(category, str)
        user = self.__find_user_information(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.donation_repository.insert_donation(
                name, category, user_information["user_id"]
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """Check user Infos and select user
        :param - user_information: Dictionary with user_id and/or user_name
        :return - Dictionary with the response of find_use use case
        """

        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_id_and_name(
                user_information["user_id"], user_information["user_name"]
            )

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_name(user_information["user_name"])

        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = self.find_user.by_id(user_information["user_id"])

        else:
            return {"Success": False, "Data": None}

        return user_founded
