#!/usr/bin/python3
"""
List all City objects from the database and display them with their State.

The script retrieves all cities ordered by cities.id and prints each line as:
<state name>: (<city id>) <city name>.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, database),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities joined with states, ordered by City.id
    rows = (
        session.query(State.name, City.id, City.name)
        .join(City, City.state_id == State.id)
        .order_by(City.id.asc())
        .all()
    )

    for state_name, city_id, city_name in rows:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
