#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
Specifically, changes the State with id = 2 to "New Mexico"
Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <user> <password> <database>")
        sys.exit(1)

    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{database}",
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).get(2)

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit() 

    session.close()
