#!/usr/bin/python3
"""Deletes all State objects containing 'a' using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Deletes states where name contains 'a'."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like("%a%")).all():
        session.delete(state)
    session.commit()

    session.close()


if __name__ == "__main__":
    main()
