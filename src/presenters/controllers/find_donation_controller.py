from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import FindDonation
from src.presenters.helpers import HttpResponse, HttpRequest
from src.presenters.errors import HttpErrors


class FindDonationController(RouteInterface):
    """ Class to define Route to find_donation use case """

    def __init__(self, find_donation_use_case: Type[FindDonation]):
        self.find_donation_use_case = find_donation_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpRequest:
        """ Method to call use case """

        response = None

        if http_request.query:
            # if query in http_request

            query_string_params = http_request.query.keys()

            if "donation_id" in query_string_params and "user_id" in query_string_params:
                donation_id = http_request.query["donation_id"]
                user_id = http_request.query["user_id"]
                response = self.find_donation_use_case.by_donation_id_and_user_id(
                    donation_id=donation_id, user_id=user_id
                )

            elif (
                "donation_id" in query_string_params and "user_id" not in query_string_params
            ):
                donation_id = http_request.query["donation_id"]
                response = self.find_donation_use_case.by_donation_id(donation_id=donation_id)

            elif (
                "user_id" in query_string_params and "donation_id" not in query_string_params
            ):
                user_id = http_request.query["user_id"]
                response = self.find_donation_use_case.by_user_id(user_id=user_id)

            elif (
                "name" in query_string_params
            ):
                name = http_request.query["name"]
                #response = self.find_donation_use_case.by_donation_id(donation_id=int(name))
                response = self.find_donation_use_case.by_donation_name(name=name)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no query in http_request
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )
