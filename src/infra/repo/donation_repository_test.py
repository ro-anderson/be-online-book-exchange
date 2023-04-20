from faker import Faker
from src.infra.entities import Donations
from src.infra.config import DBConnectionHandler
from src.infra.entities.donations import CategoryTypes
from .donation_repository import DonationRepositorySpy


faker = Faker()
donation_repository = DonationRepositorySpy()
db_connection_handler = DBConnectionHandler()


def test_insert_donation():
    """ Should insert donation in Donation table and return it """

    name = faker.name()
    category = "book"
    user_id = faker.random_number()

    # SQL Commands
    new_donation = donation_repository.insert_donation(name, category, user_id)
    engine = db_connection_handler.get_engine()
    query_user = engine.execute(
        "SELECT * FROM donations WHERE id='{}';".format(new_donation.id)
    ).fetchone()

    assert new_donation.id == query_user.id
    assert new_donation.name == query_user.name
    assert new_donation.category == query_user.category
    assert new_donation.user_id == query_user.user_id

    engine.execute("DELETE FROM donations WHERE id='{}';".format(new_donation.id))


def test_select_donation():
    """ Should select a donation in Donations table and compare it """

    donation_id = faker.random_number(digits=4)
    name = faker.name()
    category = "book"
    user_id = faker.random_number()

    category_mock = CategoryTypes("book")
    data = Donations(id=donation_id, name=name, category=category_mock, user_id=user_id)

    # SQL COmmands

    engine = db_connection_handler.get_engine()
    engine.execute(
        "INSERT INTO donations (id, name, category, user_id) VALUES ('{}', '{}', '{}', '{}');".format(
            donation_id, name, category, user_id
        )
    )
    query_donations1 = donation_repository.select_donation(donation_id=donation_id)
    query_donations2 = donation_repository.select_donation(user_id=user_id)
    query_donations3 = donation_repository.select_donation(donation_id=donation_id, user_id=user_id)

    assert data in query_donations1
    assert data in query_donations2
    assert data in query_donations3

    engine.execute("DELETE FROM donations WHERE id='{}';".format(donation_id))
