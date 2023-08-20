#!/usr/bin/python3
"""Get a state

A script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa

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

    state = session.query(State).\
        filter_by(name=sys.argv[4]).one_or_none()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
