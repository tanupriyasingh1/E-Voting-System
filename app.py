import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import get_db_connection, init_db
import os

app = Flask(__name__)
app.secret_key = 'your_super_secret_key' # In production, use environment variable

# Initialize DB on startup if it doesn't exist
if not os.path.exists('database.db'):
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        aadhar = request.form['aadhar']
        phone = request.form['phone']
        age = request.form['age']
        gender = request.form['gender']
        password = request.form['password']

        if int(age) < 18:
            flash('You must be 18 or older to register.', 'error')
            return redirect(url_for('register'))

        hashed_pw = generate_password_hash(password)
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO Voter (Name, Aadhar_no, Phone_no, Age, Gender, Password_Hash)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, aadhar, phone, age, gender, hashed_pw))
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Aadhar number already registered.', 'error')
        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        aadhar = request.form['aadhar']
        password = request.form['password']

        conn = get_db_connection()
        voter = conn.execute('SELECT * FROM Voter WHERE Aadhar_no = ?', (aadhar,)).fetchone()
        conn.close()

        if voter and check_password_hash(voter['Password_Hash'], password):
            session['voter_id'] = voter['Voter_ID']
            session['name'] = voter['Name']
            session['has_voted'] = voter['Has_Voted']
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Aadhar number or password.', 'error')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'voter_id' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))

    conn = get_db_connection()
    voter = conn.execute('SELECT * FROM Voter WHERE Voter_ID = ?', (session['voter_id'],)).fetchone()
    
    # Update session state just in case
    session['has_voted'] = voter['Has_Voted']

    candidates = conn.execute('''
        SELECT Candidate.Candidate_ID, Candidate.Name as CName, Party.Name as PName, Constituency.Name as ConstName
        FROM Candidate
        JOIN Party ON Candidate.Party_ID = Party.Party_ID
        JOIN Constituency ON Candidate.Constituency_ID = Constituency.Constituency_ID
    ''').fetchall()
    conn.close()

    return render_template('dashboard.html', candidates=candidates, has_voted=session['has_voted'])

@app.route('/vote/<int:candidate_id>', methods=['POST'])
def vote(candidate_id):
    if 'voter_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    voter = conn.execute('SELECT * FROM Voter WHERE Voter_ID = ?', (session['voter_id'],)).fetchone()
    
    if voter['Has_Voted']:
        conn.close()
        flash('You have already voted!', 'error')
        return redirect(url_for('dashboard'))

    try:
        # Cast vote
        conn.execute('INSERT INTO Vote (Voter_ID, Candidate_ID) VALUES (?, ?)', (session['voter_id'], candidate_id))
        # Update voter status
        conn.execute('UPDATE Voter SET Has_Voted = 1 WHERE Voter_ID = ?', (session['voter_id'],))
        conn.commit()
        session['has_voted'] = 1
        flash('Vote cast successfully!', 'success')
    except Exception as e:
        conn.rollback()
        flash('An error occurred while casting vote.', 'error')
    finally:
        conn.close()

    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        admin = conn.execute('SELECT * FROM Admin WHERE Username = ?', (username,)).fetchone()
        conn.close()

        if admin and check_password_hash(admin['Password_Hash'], password):
            session['admin_id'] = admin['Admin_ID']
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid admin credentials.', 'error')

    return render_template('admin_login.html')

@app.route('/admin')
def admin_dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    results = conn.execute('''
        SELECT Candidate.Name as CName, Party.Name as PName, COUNT(Vote.Vote_ID) as VoteCount
        FROM Candidate
        LEFT JOIN Vote ON Candidate.Candidate_ID = Vote.Candidate_ID
        JOIN Party ON Candidate.Party_ID = Party.Party_ID
        GROUP BY Candidate.Candidate_ID
        ORDER BY VoteCount DESC
    ''').fetchall()
    
    total_votes = conn.execute('SELECT COUNT(*) FROM Vote').fetchone()[0]
    conn.close()

    return render_template('admin.html', results=results, total_votes=total_votes)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    flash('Admin logged out.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
