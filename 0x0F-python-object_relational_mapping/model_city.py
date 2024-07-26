#!/usr/bin/python3
'''this script creates the City class'''

from model_state import Base, State
from sqlalchemy import VARCHAR, Column, Integer, String, ForeignKey


class City(Base):
    '''this is the cities table base class'''

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
