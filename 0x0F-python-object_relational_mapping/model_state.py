#!/usr/bin/python3
"""First state model

Defines a class that links to a MySQL table using SQLAlchemy

"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format("root", "root", "hbtn_0e_6_usa"),
                       pool_pre_ping=True)

Base = declarative_base()


class State(Base):
    """Class definition for states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
