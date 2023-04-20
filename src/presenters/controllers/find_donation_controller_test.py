from faker import Faker
from src.data.test import FindDonationSpy
from src.infra.test import DonationRepositorySpy
from src.presenters.helpers import HttpRequest
from .find_donation_controller import FindDonationController

faker = Faker()


def test_route():
    """ Testing route method in FindDonationController """

    find_donation_use_case = FindDonationSpy(DonationRepositorySpy())
    find_donation_router = FindDonationController(find_donation_use_case)
    attributes = {
        "donation_id": faker.random_number(digits=2),
        "user_id": faker.random_number(digits=2),
    }

    http_request = HttpRequest(query=attributes)

    http_response = find_donation_router.route(http_request)

    # Testing input
    assert (
        find_donation_use_case.by_donation_id_and_user_id_param["donation_id"] == attributes["donation_id"]
    )
    assert (
        find_donation_use_case.by_donation_id_and_user_id_param["user_id"]
        == attributes["user_id"]
    )

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_by_donation_id():
    """ Testing route method in FindDonationController """

    find_donation_use_case = FindDonationSpy(DonationRepositorySpy())
    find_donation_router = FindDonationController(find_donation_use_case)
    attributes = {"donation_id": faker.random_number(digits=2)}

    http_request = HttpRequest(query=attributes)

    http_response = find_donation_router.route(http_request)

    # Testing input
    assert find_donation_use_case.by_donation_id_param["donation_id"] == attributes["donation_id"]

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_by_user_id():
    """ Testing route method in FindDonationController """

    find_donation_use_case = FindDonationSpy(DonationRepositorySpy())
    find_donation_router = FindDonationController(find_donation_use_case)
    attributes = {"user_id": faker.random_number(digits=2)}

    http_request = HttpRequest(query=attributes)

    http_response = find_donation_router.route(http_request)

    # Testing input
    assert find_donation_use_case.by_user_id_param["user_id"] == attributes["user_id"]

    # Testing output
    assert http_response.status_code == 200
    assert "error" not in http_response.body


def test_route_error_no_query():
    """ Testing route method in FindDonationController """

    find_donation_use_case = FindDonationSpy(DonationRepositorySpy())
    find_donation_router = FindDonationController(find_donation_use_case)

    http_request = HttpRequest()

    http_response = find_donation_router.route(http_request)

    # Testing input
    assert find_donation_use_case.by_donation_id_param == {}
    assert find_donation_use_case.by_user_id_param == {}
    assert find_donation_use_case.by_donation_id_and_user_id_param == {}

    # Testing output
    assert http_response.status_code == 400
    assert "error" in http_response.body


def test_route_error_wrong_query():
    """ Testing route method in FindDonationController """

    find_donation_use_case = FindDonationSpy(DonationRepositorySpy())
    find_donation_router = FindDonationController(find_donation_use_case)

    http_request = HttpRequest(query={"something": faker.random_number(digits=2)})

    http_response = find_donation_router.route(http_request)

    # Testing input
    assert find_donation_use_case.by_donation_id_param == {}
    assert find_donation_use_case.by_user_id_param == {}
    assert find_donation_use_case.by_donation_id_and_user_id_param == {}

    # Testing output
    assert http_response.status_code == 422
    assert "error" in http_response.body
