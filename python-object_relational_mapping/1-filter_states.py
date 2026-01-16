#!/usr/bin/python3
"""Lists states starting with 'N' from a database using MySQLdb."""

import sys
import MySQLdb


def main():
    """Connects to MySQL and prints states whose name starts with 'N'."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
