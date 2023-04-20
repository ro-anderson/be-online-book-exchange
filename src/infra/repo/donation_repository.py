# pylint: disable=E1101

from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import text
from src.data.interfaces import DonationRepositorySpy
from src.domain.models import Donations
from src.infra.config import DBConnectionHandler
from src.infra.config import func
from src.infra.entities import Donations as DonationsModel
from fuzzywuzzy import fuzz
import re


def clean_string(value):
    cleaned_value = re.sub(r'[^\w\s]', '', value)  # Remove all non-alphanumeric and non-whitespace characters
    cleaned_value = cleaned_value.lower()          # Convert to lowercase
    return cleaned_value

def string_similarity(str1, str2):
    return fuzz.ratio(str1, str2)

class DonationRepositorySpy(DonationRepositorySpy):
    """ Class to manage Donation Repository """

    @classmethod
    def insert_donation(cls, name: str, category: str, user_id: int) -> Donations:
        """
        Insert data in DonationsEntity entity
        :param - name: name of the donation
               - category: Enum with categorys acepted
               - user_id: id of the owner (FK)
        :return - tuple with new donation inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_donation = DonationsModel(name=name, category=category, user_id=user_id)
                db_connection.session.add(new_donation)
                db_connection.session.commit()

                return Donations(
                    id=new_donation.id,
                    name=new_donation.name,
                    category=new_donation.category.value,
                    user_id=new_donation.user_id,
                )

            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_donation(cls, donation_id: int = None, user_id: int = None, name: str = None) -> List[Donations]:
        """
        Select data in DonationsEntity entity by id and/or user_id
        :param - donation_id: Id of the donation registry
               - user_ud: Id of the owner
        :return - List with Donations selected
        """

        try:

            query_data = None

            if donation_id and not user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(DonationsModel)
                        .filter_by(id=donation_id)
                        .one()
                    )
                    query_data = [data]

            elif not donation_id and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(DonationsModel)
                        .filter_by(user_id=user_id)
                        .all()
                    )
                    query_data = data

            elif donation_id and user_id:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(DonationsModel)
                        .filter_by(id=donation_id, user_id=user_id)
                        .one()
                    )
                    query_data = [data]

            elif name:

                with DBConnectionHandler() as db_connection:

                    engine = db_connection.get_engine()
                    conn = engine.connect() 

                    conn.connection.create_function('clean_string', 1, clean_string)
                    conn.connection.create_function('string_similarity', 2, string_similarity)

                    query = """
                    SELECT
                        donations.id AS donations_id,
                        donations.name AS donations_name,
                        donations.category AS donations_category,
                        donations.user_id AS donations_user_id,
                        string_similarity(clean_string(donations.name), clean_string(:name)) AS similarity
                    FROM
                        donations
                    ORDER BY
                        string_similarity(donations.name, :name) DESC;
                    """

                    result_proxy = conn.execute(text(query), {'name': name})
                    data = result_proxy.fetchall()
                    
                    # Filtering by most similar donations names
                    similarity_threshhold = 50
                    data = [tu for tu in data if tu[-1] > similarity_threshhold]

                    # transform the list of tuple into list of DonationsModel
                    data = [cls.select_donation(donation_tuple[0])[0] for donation_tuple in data]
                    
                    

                    query_data = data

            return query_data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
