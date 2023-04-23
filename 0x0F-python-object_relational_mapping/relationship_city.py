#!/usr/bin/python3
"""This script contains the class definition of a City"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class that is mapped to the cities
    table in the hbtn_0e_6_usa database"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
