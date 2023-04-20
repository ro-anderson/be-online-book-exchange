from src.infra.repo.donation_repository import DonationRepositorySpy
from src.infra.repo.user_repository import UserRepository
from src.data.register_donation import RegisterDonation
from src.data.find_user import FindUser
from src.presenters.controllers import RegisterDonationController


def register_donation_composer() -> RegisterDonationController:
    """Composing Register Donation Route
    :param - None
    :return - Object with Register Donation Route
    """

    repository = DonationRepositorySpy()
    find_user_use_case = FindUser(UserRepository())
    use_case = RegisterDonation(repository, find_user_use_case)
    register_donation_route = RegisterDonationController(use_case)

    return register_donation_route
