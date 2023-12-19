#!/usr/bin/python3
"""This script adds the State object
“Louisiana” to the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username, password, db_name = sys.argv[1:]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
