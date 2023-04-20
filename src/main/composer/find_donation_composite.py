from src.presenters.controllers import FindDonationController
from src.data.find_donation import FindDonation
from src.infra.repo.donation_repository import DonationRepositorySpy


def find_donation_composer() -> FindDonationController:
    """Composing Find Donation Route
    :param - None
    :return - Object with Find Donation Route
    """

    repository = DonationRepositorySpy()
    use_case = FindDonation(repository)
    find_donation_route = FindDonationController(use_case)

    return find_donation_route
