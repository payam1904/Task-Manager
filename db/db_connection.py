import sqlite3 as sql


try:
    with sql.connect("db/database.db") as database:
        admin = database.cursor()

except sql.OperationalError as error:
    print(f"Connection Failed!, {error}")

