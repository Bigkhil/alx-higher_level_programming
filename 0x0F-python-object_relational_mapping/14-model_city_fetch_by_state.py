#!/usr/bin/python3
'''this script prints all city objects from the database'''
import MySQLdb
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    '''main function to execute when using the script'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
                                   ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()
    for row in rows:
        print(f"{row.State.name}: ({row.City.id}) {row.City.name}")
    session.close()


if __name__ == "__main__":
    main()
