#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

"""
Script that connects to running server and lists all state objects
"""

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    conn = "mysql://{}:{}@localhost:3306/{}".format(\
        username, password, database)

    engine = create_engine(conn)
    
    Session = sessionmaker(bind=engine)

    session = Session()

    
    for state in session.query(State).all:
        print("{}: {}".format(state.id, state.name))

