#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>
If the table is empty, prints 'Nothing'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import State class and Base

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <user> <password> <database>")
        sys.exit(1)

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL using SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost/{database}",
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Instantiate a Session
    session = Session()

    # Query the first State object ordered by id ascending
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
