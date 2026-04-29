import sqlite3
import random

#Work between Thaice, Franklin and Claudio Hernandez
conn = sqlite3.connect("cinema.db", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = ON")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        idUser  INTEGER PRIMARY KEY AUTOINCREMENT,
        Cedula  VARCHAR(20)  UNIQUE NOT NULL,
        Name    VARCHAR(100) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Movies (
        idMovie     INTEGER PRIMARY KEY AUTOINCREMENT,
        TMDB_ID     INTEGER      UNIQUE NOT NULL,
        Title       VARCHAR(255) NOT NULL,
        Description TEXT,
        Language    VARCHAR(5),
        PosterPath  VARCHAR(255),
        Genre       VARCHAR(100)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Screenings (
        idScreening INTEGER PRIMARY KEY AUTOINCREMENT,
        idMovie     INTEGER     NOT NULL,
        Hour        VARCHAR(8)  NOT NULL,
        UNIQUE(idMovie, Hour),
        FOREIGN KEY (idMovie) REFERENCES Movies(idMovie)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Seats (
        idSeat   INTEGER PRIMARY KEY AUTOINCREMENT,
        SeatName VARCHAR(4) UNIQUE NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Reservations (
        idReservation INTEGER PRIMARY KEY AUTOINCREMENT,
        idUser        INTEGER     NOT NULL,
        idScreening   INTEGER     NOT NULL,
        OrderID       VARCHAR(50) UNIQUE NOT NULL,
        FOREIGN KEY (idUser)      REFERENCES Users(idUser),
        FOREIGN KEY (idScreening) REFERENCES Screenings(idScreening)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ReservationSeats (
        idReservation INTEGER NOT NULL,
        idSeat        INTEGER NOT NULL,
        PRIMARY KEY (idReservation, idSeat),
        FOREIGN KEY (idReservation) REFERENCES Reservations(idReservation),
        FOREIGN KEY (idSeat)        REFERENCES Seats(idSeat)
    )
""")

conn.commit()


for row in ['A', 'B', 'C', 'D', 'E', 'F']:
    for num in range(1, 13):
        cursor.execute(
            "INSERT OR IGNORE INTO Seats (SeatName) VALUES (?)",
            (f"{row}{num}",)
        )
conn.commit()


#Users

def createuser(cedula: str, name: str):
    cursor.execute(
        "INSERT OR IGNORE INTO Users (Cedula, Name) VALUES (?, ?)",
        (cedula, name)
    )
    conn.commit()
   
    cursor.execute("SELECT idUser FROM Users WHERE Cedula = ?", (cedula,))
    return cursor.fetchone()[0]


def getuserbycedula(cedula: str):
    cursor.execute("SELECT * FROM Users WHERE Cedula = ?", (cedula,))
    return cursor.fetchone()

#Movies

def savemovie(tmdb_id: int, title: str, description: str,
               language: str, poster_path: str, genre: str = "Unknown"):
    cursor.execute("""
        INSERT OR IGNORE INTO Movies (TMDB_ID, Title, Description, Language, PosterPath, Genre)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (tmdb_id, title, description, language, poster_path, genre))
    conn.commit()
    cursor.execute("SELECT idMovie FROM Movies WHERE TMDB_ID = ?", (tmdb_id,))
    return cursor.fetchone()[0]


def getmoviebytmdb(tmdb_id: int):
    cursor.execute("SELECT * FROM Movies WHERE TMDB_ID = ?", (tmdb_id,))
    return cursor.fetchone()


def getallmovies():
    
    cursor.execute("SELECT * FROM Movies")
    return cursor.fetchall()

#Screenings

def savescreening(movie_id: int, hour: str):
    cursor.execute(
        "SELECT idScreening FROM Screenings WHERE idMovie = ? AND Hour = ?",
        (movie_id, hour)
    )
    row = cursor.fetchone()
    if row:
        return row[0]

    cursor.execute(
        "INSERT INTO Screenings (idMovie, Hour) VALUES (?, ?)",
        (movie_id, hour)
    )
    conn.commit()
    return cursor.lastrowid

def getscreeningsformovie(movie_id: int):
    cursor.execute(
        "SELECT idScreening, Hour FROM Screenings WHERE idMovie = ?",
        (movie_id,)
    )
    return cursor.fetchall()

#Seats

def gettakenseats(screening_id: int):
    cursor.execute("""
        SELECT s.SeatName
        FROM ReservationSeats rs
        JOIN Seats s ON rs.idSeat = s.idSeat
        JOIN Reservations r ON rs.idReservation = r.idReservation
        WHERE r.idScreening = ?
    """, (screening_id,))
    return [row[0] for row in cursor.fetchall()]


#Reservations
def createreservation(user_id: int, screening_id: int, seat_names: list):
    order_id = f"{user_id}-D{random.randint(1000000, 9999999)}B"

    cursor.execute("""
        INSERT INTO Reservations (idUser, idScreening, OrderID)
        VALUES (?, ?, ?)
    """, (user_id, screening_id, order_id))
    reservation_id = cursor.lastrowid

    for seat_name in seat_names:
        cursor.execute(
            "SELECT idSeat FROM Seats WHERE SeatName = ?", (seat_name,)
        )
        row = cursor.fetchone()
        if row:
            cursor.execute("""
                INSERT INTO ReservationSeats (idReservation, idSeat)
                VALUES (?, ?)
            """, (reservation_id, row[0]))

    conn.commit()
    return order_id


def getreservationsbyuser(user_id: int):
    cursor.execute("""
        SELECT r.OrderID, m.Title, sc.Hour
        FROM Reservations r
        JOIN Screenings sc ON r.idScreening = sc.idScreening
        JOIN Movies m      ON sc.idMovie    = m.idMovie
        WHERE r.idUser = ?
        ORDER BY r.idReservation DESC
    """, (user_id,))
    return cursor.fetchall()


def getseatsforreservation(order_id: str):
    
    cursor.execute("""
        SELECT s.SeatName
        FROM ReservationSeats rs
        JOIN Seats s         ON rs.idSeat        = s.idSeat
        JOIN Reservations r  ON rs.idReservation = r.idReservation
        WHERE r.OrderID = ?
    """, (order_id,))
    return [row[0] for row in cursor.fetchall()]


#STATUS

currentuserid = None
currentmovieid = None
currentscreeningid = None
