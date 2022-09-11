#!/usr/bin/python3
"""This script prints the State object with the name of
the state passed as an argument to the script"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State, Base

    username, password, database, state_name = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).all()

    if not state:
        print("Not found")
    else:
        print(state[0].id)
