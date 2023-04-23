#!/usr/bin/python3
"""This script lists all State objects,and corresponding
 City objects, contained in the database hbtn_0e_101_usa"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import State, Base

    username, password, db_name = sys.argv[1:]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).\
            order_by(State.id).\
            order_by(State.id).all():

        print(f'{state.id}: {state.name}')
        [print(f'   {city.id}: {city.name}') for city in state.cities]
