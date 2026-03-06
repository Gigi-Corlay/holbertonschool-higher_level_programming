#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>
Results are sorted by states.id
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State from model_state

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <user> <password> <database>")
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the SQLAlchemy engine to connect to MySQL
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session instance
    session = Session()

    # Query all State objects, ordered by id ascending
    states = session.query(State).order_by(State.id).all()

    # Display results in the format: <id>: <name>
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
