#!/usr/bin/python3
"""This script that prints all City objects
from the database hbtn_0e_14_usa"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username, password, db_name = sys.argv[1:]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(
        State.name, City.id, City.name).order_by(City.id).all()

    for state, city_id, city in rows:
        print(f'{state}: ({city_id}) {city}')
