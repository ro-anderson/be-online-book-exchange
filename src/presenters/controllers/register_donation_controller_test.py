from faker import Faker
from src.data.test import RegisterDonationSpy
from src.presenters.helpers import HttpRequest
from src.infra.test import DonationRepositorySpy, UserRepositorySpy
from .register_donation_controller import RegisterDonationController

faker = Faker()


def test_route():
    """ Testing route method in RegisterUserRouter """

    register_donation_use_case = RegisterDonationSpy(DonationRepositorySpy(), UserRepositorySpy())
    register_donation_router = RegisterDonationController(register_donation_use_case)
    attributes = {
        "name": faker.word(),
        "category": "Dog",
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_donation_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_donation_use_case.registry_param["name"] == attributes["name"]
    assert register_donation_use_case.registry_param["category"] == attributes["category"]
    assert (
        register_donation_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_without_age():
    """ Testing route method in RegisterUserRouter """

    register_donation_use_case = RegisterDonationSpy(DonationRepositorySpy(), UserRepositorySpy())
    register_donation_router = RegisterDonationController(register_donation_use_case)
    attributes = {
        "name": faker.word(),
        "category": "Dog",
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_donation_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_donation_use_case.registry_param["name"] == attributes["name"]
    assert register_donation_use_case.registry_param["category"] == attributes["category"]
    assert (
        register_donation_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_user_id_in_user_information():
    """ Testing route method in RegisterUserRouter """

    register_donation_use_case = RegisterDonationSpy(DonationRepositorySpy(), UserRepositorySpy())
    register_donation_router = RegisterDonationController(register_donation_use_case)

    attributes = {
        "name": faker.word(),
        "category": "Dog",
        "user_information": {"user_name": faker.word()},
    }

    response = register_donation_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_donation_use_case.registry_param["name"] == attributes["name"]
    assert register_donation_use_case.registry_param["category"] == attributes["category"]
    assert (
        register_donation_use_case.registry_param["user_information"]
        == attributes["user_information"]
    )

    # Testing output
    assert response.status_code == 200
    assert "error" not in response.body


def test_route_error_no_body():
    """ Testing route method in RegisterUserRouter """

    register_donation_use_case = RegisterDonationSpy(DonationRepositorySpy(), UserRepositorySpy())
    register_donation_router = RegisterDonationController(register_donation_use_case)

    response = register_donation_router.route(HttpRequest())

    # Testing input
    assert register_donation_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 400
    assert "error" in response.body


def test_route_error_wrong_body():
    """ Testing route method in RegisterUserRouter """

    register_donation_use_case = RegisterDonationSpy(DonationRepositorySpy(), UserRepositorySpy())
    register_donation_router = RegisterDonationController(register_donation_use_case)

    attributes = {
        "category": "Dog",
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_donation_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_donation_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body


def test_route_error_wrong_user_information():
    """ Testing route method in RegisterUserRouter """

    register_donation_use_case = RegisterDonationSpy(DonationRepositorySpy(), UserRepositorySpy())
    register_donation_router = RegisterDonationController(register_donation_use_case)

    attributes = {"name": faker.word(), "category": "Dog", "user_information": {}}

    response = register_donation_router.route(HttpRequest(body=attributes))

    # Testing input
    assert register_donation_use_case.registry_param == {}

    # Testing output
    assert response.status_code == 422
    assert "error" in response.body
