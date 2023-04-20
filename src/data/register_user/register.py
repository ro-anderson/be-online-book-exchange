from typing import Type, Dict
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.domain.models import Users


class RegisterUser(RegisterUserInterface):
    """ Class to define usercase: Register User """

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def register(self, name: str, email: str) -> Dict[bool, Users]:
        """Register user use case
        :param - name: person name
               - email: email of the person
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(email, str)

        if validate_entry:
            response = self.user_repository.insert_user(name, email)

        return {"Success": validate_entry, "Data": response}
