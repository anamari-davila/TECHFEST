import sqlite3

conn = sqlite3.connect("crepe_stand.db")
conn.execute("PRAGMA foreign_keys = ON")  # enable FK enforcement

cursor = conn.cursor()

createTablesQuery = """
    CREATE TABLE IF NOT EXISTS Movies(
        idMovie INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Hour VARCHAR(8)
    );

    CREATE TABLE IF NOT EXISTS Seats(
        idSeats INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Name VARCHAR(3)
    );

    CREATE TABLE IF NOT EXISTS Reservations(
        idReservation INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        idMovie INTEGER NOT NULL,
        idSeats INTEGER NOT NULL,
        Hour VARCHAR(8),
        FOREIGN KEY (idMovie) REFERENCES Movies(idMovie),
        FOREIGN KEY (idSeats) REFERENCES Seats(idSeats)
    );

    CREATE TABLE IF NOT EXISTS Room(
        idRoom INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Room VARCHAR(2),
        idMovie INTEGER NOT NULL,
        Seat INTEGER NOT NULL,
        FOREIGN KEY (idMovie) REFERENCES Movies(idMovie),
        FOREIGN KEY (Seat) REFERENCES Seats(idSeats)
    );
"""

cursor.executescript(createTablesQuery)
conn.commit()
conn.close()