#!/usr/bin/python3
"""First state

A script that prints the first State object from the database hbtn_0e_6_usa
using SQLAlchemy

"""
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).\
            filter(State.name.like('%a%')).\
            order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
