#!/usr/bin/python3
"""Displays states matching a name (unsafe by design) using MySQLdb."""

import sys
import MySQLdb


def main():
    """Connects to MySQL and prints matching states ordered by id."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()

    # Case-sensitive exact match using BINARY
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
    ).format(sys.argv[4])

    cur.execute(query)
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
