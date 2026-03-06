#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import Base and State class

if __name__ == "__main__":
    # Check number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <user> <password> <database>")
        sys.exit(1)

    # Assign arguments
    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL using SQLAlchemy
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{database}",
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the change to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()
