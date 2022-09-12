#!/usr/bin/python3
"""This script prints the first state object from
the database hbtn_0e_6_usa"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    username, password, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")