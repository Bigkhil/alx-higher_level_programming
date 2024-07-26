#!/usr/bin/python3
'''
11-model_state_insert.py: script that adds the State object "Louisiana" to the
database hbtn_0e_6_usa
Usage: ./11-model_state_insert.py <mysql username> <mysql password>
<database name>
'''

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).filter(
        State.id == City.state_id).order_by(State.id).all()

    for row in results:
        print('{}: ({}) {}'.format(row.State.name, row.City.id, row.City.name))

    session.close()
