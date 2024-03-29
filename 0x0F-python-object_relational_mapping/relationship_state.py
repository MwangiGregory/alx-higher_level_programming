#!/usr/bin/python3
"""This script contains the class definition of a State"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Class that is mapped to the states
    table in the hbtn_0e_6_usa database"""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", cascade="all, delete, delete-orphan", backref="state")
