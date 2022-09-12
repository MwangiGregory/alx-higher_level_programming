#!/usr/bin/python3
"""This module defines a city model"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """Definition for a City model that maps
    to a city table"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
