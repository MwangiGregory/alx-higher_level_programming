#!/usr/bin/python3
"""This script prints the State object with the
 name passed as argument from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username, password, db_name, state_name = sys.argv[1:]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id).filter_by(name=state_name).one_or_none()
    if (state):
        print(f'{state.id}')
    else:
        print('Not found')
