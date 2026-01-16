#!/usr/bin/python3
"""Creates the states table in the given database using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from model_state import Base


def main():
    """Creates all tables for imported models."""
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
