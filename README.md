# E-Voting System (DBMS Project)

A secure, database-driven electronic voting system built with Python, Flask, and SQLite. This project was designed to simplify and secure the voting process, ensuring a "one person, one vote" mechanism through proper authentication and database constraints.

## Features
- **Secure Registration & Login**: Voters register using their Aadhar number and log in securely.
- **Biometric Simulation**: Includes an interactive UI simulation for fingerprint scanning before casting a vote.
- **Vote Integrity**: Database constraints ensure users can only cast a single vote.
- **Admin Dashboard**: Real-time tracking of election results and vote shares.
- **Modern UI**: Clean, responsive Glassmorphism design with a fully functional Dark Mode.

## Technology Stack
- **Backend**: Python 3, Flask
- **Database**: SQLite (6 Normalized Tables: Voter, Party, Constituency, Candidate, Vote, Admin)
- **Frontend**: HTML5, Vanilla CSS, Vanilla JavaScript
- **Security**: Werkzeug Password Hashing, Flask Sessions

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd evoting_system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   This script will create the `database.db` file and seed it with initial data (Admin account, Indian Political Parties, and Constituencies).
   ```bash
   python models.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Default Credentials
- **Admin Username**: `admin`
- **Admin Password**: `admin123`
