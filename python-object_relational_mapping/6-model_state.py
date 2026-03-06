#!/usr/bin/python3
"""
Creates the states table in the database using SQLAlchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py <user> <password> <database>")
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL using SQLAlchemy
    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    # Create all tables (State) that inherit from Base
    Base.metadata.create_all(engine)
