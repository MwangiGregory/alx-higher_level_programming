#!/usr/bin/python3
"""This script lists all the State objects from the
hbtn_0e_6_usa database"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    username, passwd, database = sys.argv[1:]
    db_url = f"mysql+mysqldb://{username}:{passwd}\
               @localhost/{database}"
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    print(session)
    for instance in session.query(State).order_by(State.id):
        print(f"{instance.id}: {instance.name}")
