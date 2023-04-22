#!/usr/bin/python3
"""This script prints the first State
object from the database hbtn_0e_6_usa"""

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

    first_state = session.query(State).order_by(State.id).first()
    if (first_state):
        print(f'{first_state.id}: {first_state.name}')
    else:
        print("Nothing")
