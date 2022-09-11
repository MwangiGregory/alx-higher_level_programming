#!/usr/bin/python3
"""This module defines a state model that links to a
table called states in the hbtn_0e_6_usa database"""


import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class State(Base):
    """Definition of class State that maps to states table"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True,
                unique=True)
    name = Column(String(128), nullable=False)
