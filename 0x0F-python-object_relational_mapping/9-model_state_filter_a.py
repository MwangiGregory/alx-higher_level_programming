#!/usr/bin/python3
"""This script lists all State objects that
 contain the letter a from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username, password, db_name = sys.argv[1:]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).filter(
        State.name.like('%a%'))
    for state in states:
        print(f'{state.id}: {state.name}')
