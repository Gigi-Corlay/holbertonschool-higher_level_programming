#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name>
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check number of arguments first
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <user> <password> <database> <state name>")
        sys.exit(1)

    # Assign arguments
    user, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL using SQLAlchemy
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{database}",
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state by name (SQL injection safe)
    state = session.query(State).filter(State.name == state_name).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
