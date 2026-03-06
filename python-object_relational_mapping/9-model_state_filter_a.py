#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa
Usage: ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>
Results are sorted by states.id in ascending order.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State 

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <user> <password> <database>")
        sys.exit(1)

    user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{database}",
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")


    session.close()
