#!/usr/bin/python3
'''this script creates a state model using sqlalchemy'''
import MySQLdb
from sqlalchemy import create_engine, VARCHAR, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    '''state class that links to mysql table states'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
