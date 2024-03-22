#!/usr/bin/python3
""" lists all State objects """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Access to the database and get the states
    from the database. """

    dtb = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(dtb)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print('{0}: {1}'.format(state.id, state.name))
    else:
        print("Nothing")