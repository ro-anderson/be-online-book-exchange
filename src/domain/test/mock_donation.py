from faker import Faker
from src.domain.models import Donations

faker = Faker()


def mock_donation() -> Donations:
    """Mocking Donation
    :param - None
    :return - Fake Donation registry
    """

    return Donations(
        id=faker.random_number(digits=5),
        name=faker.name(),
        category="book",
        user_id=faker.random_number(digits=5),
    )
