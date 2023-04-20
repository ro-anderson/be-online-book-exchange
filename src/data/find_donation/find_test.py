from faker import Faker
from src.infra.test import DonationRepositorySpy
from .find import FindDonation

faker = Faker()


def test_by_donation_id():
    """ Testing donation_id method in FindDonation """

    donation_repo = DonationRepositorySpy()
    find_donation = FindDonation(donation_repo)

    attribute = {"donation_id": faker.random_number(digits=2)}
    response = find_donation.by_donation_id(donation_id=attribute["donation_id"])

    # Testing Input
    assert donation_repo.select_donation_param["donation_id"] == attribute["donation_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_donation_id():
    """ Testing donation_id fail method in FindDonation """

    donation_repo = DonationRepositorySpy()
    find_donation = FindDonation(donation_repo)

    attribute = {"donation_id": faker.word()}
    response = find_donation.by_donation_id(donation_id=attribute["donation_id"])

    # Testing Input
    assert donation_repo.select_donation_param == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_user_id():
    """ Testing by_id method in FindDonation """

    donation_repo = DonationRepositorySpy()
    find_donation = FindDonation(donation_repo)

    attribute = {"user_id": faker.random_number(digits=2)}
    response = find_donation.by_user_id(user_id=attribute["user_id"])

    # Testing Input
    assert donation_repo.select_donation_param["user_id"] == attribute["user_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_user_id():
    """ Testing by_id fail method in FindDonation """

    donation_repo = DonationRepositorySpy()
    find_donation = FindDonation(donation_repo)

    attribute = {"user_id": faker.word()}
    response = find_donation.by_user_id(user_id=attribute["user_id"])

    # Testing Input
    assert donation_repo.select_donation_param == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def test_by_donation_id_and_user_id():
    """ Testing by_donation_id_and_user_id method in FindDonation """

    donation_repo = DonationRepositorySpy()
    find_donation = FindDonation(donation_repo)

    attribute = {
        "user_id": faker.random_number(digits=2),
        "donation_id": faker.random_number(digits=2),
    }
    response = find_donation.by_donation_id_and_user_id(
        user_id=attribute["user_id"], donation_id=attribute["donation_id"]
    )

    # Testing Input
    assert donation_repo.select_donation_param["user_id"] == attribute["user_id"]
    assert donation_repo.select_donation_param["donation_id"] == attribute["donation_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def test_fail_by_donation_id_and_user_id():
    """ Testing by_donation_id_and_user_id fail method in FindDonation """

    donation_repo = DonationRepositorySpy()
    find_donation = FindDonation(donation_repo)

    attribute = {"user_id": faker.word(), "donation_id": faker.word()}
    response = find_donation.by_donation_id_and_user_id(
        user_id=attribute["user_id"], donation_id=attribute["donation_id"]
    )

    # Testing Input
    assert donation_repo.select_donation_param == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
