import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = 'database.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Voter Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Voter (
            Voter_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Aadhar_no TEXT UNIQUE NOT NULL,
            Phone_no TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Gender TEXT NOT NULL,
            Password_Hash TEXT NOT NULL,
            Has_Voted BOOLEAN DEFAULT 0
        )
    ''')

    # 2. Party Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Party (
            Party_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Symbol_URL TEXT
        )
    ''')

    # 3. Constituency Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Constituency (
            Constituency_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            State TEXT NOT NULL
        )
    ''')

    # 4. Candidate Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Candidate (
            Candidate_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Party_ID INTEGER,
            Constituency_ID INTEGER,
            FOREIGN KEY(Party_ID) REFERENCES Party(Party_ID),
            FOREIGN KEY(Constituency_ID) REFERENCES Constituency(Constituency_ID)
        )
    ''')

    # 5. Vote Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vote (
            Vote_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Voter_ID INTEGER,
            Candidate_ID INTEGER,
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(Voter_ID) REFERENCES Voter(Voter_ID),
            FOREIGN KEY(Candidate_ID) REFERENCES Candidate(Candidate_ID)
        )
    ''')

    # 6. Admin Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Admin (
            Admin_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT UNIQUE NOT NULL,
            Password_Hash TEXT NOT NULL
        )
    ''')

    conn.commit()
    seed_data(conn, cursor)
    conn.close()

def seed_data(conn, cursor):
    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM Admin")
    if cursor.fetchone()[0] > 0:
        return

    # Seed Admin
    admin_pw = generate_password_hash('admin123')
    cursor.execute("INSERT INTO Admin (Username, Password_Hash) VALUES (?, ?)", ('admin', admin_pw))

    # Seed Parties
    parties = [
        ('Bharatiya Janata Party (BJP)', 'lotus.png'),
        ('Indian National Congress (INC)', 'hand.png'),
        ('Aam Aadmi Party (AAP)', 'broom.png'),
        ('Independent', 'independent.png')
    ]
    cursor.executemany("INSERT INTO Party (Name, Symbol_URL) VALUES (?, ?)", parties)

    # Seed Constituencies
    constituencies = [
        ('New Delhi', 'Delhi'),
        ('Varanasi', 'Uttar Pradesh'),
        ('Wayanad', 'Kerala'),
        ('Gandhinagar', 'Gujarat')
    ]
    cursor.executemany("INSERT INTO Constituency (Name, State) VALUES (?, ?)", constituencies)

    # Seed Candidates
    candidates = [
        ('Narendra Modi', 1, 2), # BJP, Varanasi
        ('Rahul Gandhi', 2, 3),  # INC, Wayanad
        ('Arvind Kejriwal', 3, 1), # AAP, New Delhi
        ('Amit Shah', 1, 4), # BJP, Gandhinagar
        ('Ajay Maken', 2, 1) # INC, New Delhi
    ]
    cursor.executemany("INSERT INTO Candidate (Name, Party_ID, Constituency_ID) VALUES (?, ?, ?)", candidates)

    conn.commit()

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully.")
