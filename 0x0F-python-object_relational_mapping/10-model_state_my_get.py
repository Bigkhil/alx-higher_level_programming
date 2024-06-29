#!/usr/bin/python3
'''this script should list all states in the database using sqlalchemy'''
import MySQLdb
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    '''main fucntion to execute when using the script'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]
                                   ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).filter(State.name == sys.argv[4]).one()
    if rows:
        print(rows.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
