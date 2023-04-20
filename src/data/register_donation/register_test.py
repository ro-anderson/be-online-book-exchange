from faker import Faker
from src.infra.test import DonationRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy
from .register import RegisterDonation

faker = Faker()


def test_registry():
    """ Testing Registru method in RegisterDonation """

    donation_repo = DonationRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_donation = RegisterDonation(donation_repo, find_user)

    attributes = {
        "name": faker.name(),
        "category": faker.name(),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }

    response = register_donation.registry(
        name=attributes["name"],
        category=attributes["category"],
        user_information=attributes["user_information"],
    )

    # Testing Inputs
    assert donation_repo.insert_donation_param["name"] == attributes["name"]
    assert donation_repo.insert_donation_param["category"] == attributes["category"]

    # Testing FindUser Inputs
    assert (
        find_user.by_id_and_name_param["user_id"]
        == attributes["user_information"]["user_id"]
    )
    assert (
        find_user.by_id_and_name_param["name"]
        == attributes["user_information"]["user_name"]
    )

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]
