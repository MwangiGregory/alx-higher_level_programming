#!/usr/bin/python3
"""This script prints all City objects
from the database hbtn_0e_14_usa"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City, Base
    from model_state import State

    username, password, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name)\
        .join(State).order_by(City.id).all()
    for state_name, city_id, city_name in cities:
        print(f'{state_name}: ({city_id}) {city_name}')
