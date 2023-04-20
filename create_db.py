from src.infra.config import *
from src.infra.entities import *

if __name__ == '__main__':
    db_conn = DBConnectionHandler()
    engine = db_conn.get_engine()
    print(engine, Users, Donations)
    Base.metadata.create_all(engine)

