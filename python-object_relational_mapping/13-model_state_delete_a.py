#!/usr/bin/python3
""" lists all State objects """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Access to the database and get the states
    from the database. """

    username = argv[1]
    password = argv[2]
    database = argv[3]

    dtb = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database)

    engine = create_engine(dtb)
    Session = sessionmaker(bind=engine)

    session = Session()

    for state in session.query(State).filter(State.name.contains('a')):
        session.delete(state)
    session.commit()
