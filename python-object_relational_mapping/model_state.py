#!/usr/bin/python3
"""
Contains the class definition of a State and an instance 
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create Base instance for declarative system
Base = declarative_base()

class State(Base):
    """
    State class linked to the 'states' table in MySQL
    """
    __tablename__ = 'states'  # Name of the MySQL table

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
