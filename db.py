import sqlite3

conn = sqlite3.connect("cinema.db", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        idUser INTEGER PRIMARY KEY AUTOINCREMENT,
        Cedula VARCHAR(20) UNIQUE NOT NULL,
        Name   VARCHAR(100) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Movies(
        idMovie     INTEGER PRIMARY KEY AUTOINCREMENT,
        TMDB_ID     INTEGER UNIQUE NOT NULL,
        Title       VARCHAR(255) NOT NULL,
        Description TEXT,
        Language    VARCHAR(5),
        PosterPath  VARCHAR(255)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Screenings(
        idScreening INTEGER PRIMARY KEY AUTOINCREMENT,
        idMovie     INTEGER NOT NULL,
        Hour        VARCHAR(8) NOT NULL,
        UNIQUE(idMovie, Hour)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Seats(
        idSeat   INTEGER PRIMARY KEY AUTOINCREMENT,
        SeatName VARCHAR(3) UNIQUE NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Reservations(
        idReservation INTEGER PRIMARY KEY AUTOINCREMENT,
        idUser        INTEGER NOT NULL,
        idScreening   INTEGER NOT NULL,
        OrderID       VARCHAR(50) UNIQUE NOT NULL,
        
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ReservationSeats(
        idReservation INTEGER NOT NULL,
        idSeat        INTEGER NOT NULL,
        PRIMARY KEY(idReservation, idSeat)
    )
""")

conn.commit()

rows = ['A', 'B', 'C', 'D', 'E', 'F']
for r in rows:
    for n in range(1, 13):
        seat_name = f"{r}{n}"
        cursor.execute("INSERT OR IGNORE INTO Seats(SeatName) VALUES(?)", (seat_name,))
conn.commit()

current_user_id = None
current_movie_id = None
current_screening_id = None
taken_seats = []