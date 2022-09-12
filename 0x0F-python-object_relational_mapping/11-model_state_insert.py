#!/usr/bin/python3
"""This script adds the state object "Lousiana to
hbtn_0e_6_usa database"""


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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
