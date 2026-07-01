<h1 align="center">E-Voting System 🗳️</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.3.3-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey.svg" alt="Database">
  <img src="https://img.shields.io/badge/Deployed-Vercel-black.svg" alt="Deployed on Vercel">
</p>

<p align="center">
  <strong>A secure, database-driven electronic voting system designed to simplify and secure the voting process.</strong>
  <br>
  <i>Built for the modern web with a focus on "one person, one vote" integrity.</i>
</p>

---

## 🌐 Live Demo

You can view and test the live application here:
**[View Live Project on Vercel](#)** *(Replace this `#` with your actual Vercel link!)*

---

## ✨ Key Features

- **Secure Registration & Login**: Voters register using their Aadhar number. Passwords are securely hashed.
- **Biometric Simulation**: Includes an interactive UI simulation for fingerprint scanning before casting a vote.
- **Vote Integrity**: Strong database constraints ensure users can only cast a single vote.
- **Admin Dashboard**: Real-time tracking of election results, vote shares, and total turnout.
- **Modern UI/UX**: Clean, responsive Glassmorphism design featuring a fully functional Dark Mode.
- **Serverless Ready**: Configured for seamless deployment on Vercel using temporary in-memory database storage.

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Database**: SQLite (6 Normalized Tables: `Voter`, `Party`, `Constituency`, `Candidate`, `Vote`, `Admin`)
- **Frontend**: HTML5, Vanilla CSS, Vanilla JavaScript
- **Security**: Werkzeug Password Hashing, Flask Sessions
- **Deployment**: Vercel Serverless Functions

## 📸 Screenshots

*(You can add screenshots of your project here to make your portfolio stand out)*

<details>
<summary>Click to view screenshots</summary>
<br>

| Login Page | Voting Dashboard | Admin Panel |
| :---: | :---: | :---: |
| *(Add image link)* | *(Add image link)* | *(Add image link)* |

</details>

## 🚀 Local Setup Instructions

Want to run this project locally? Follow these steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/tanupriyasingh1/E-Voting-System.git
   cd E-Voting-System
   ```

2. **Create and activate a virtual environment**
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

## 🔐 Default Credentials

To access the admin dashboard, go to `/admin/login` and use:
- **Admin Username**: `admin`
- **Admin Password**: `admin123`

## 📂 Project Structure

```text
E-Voting-System/
├── static/
│   ├── css/           # Styling (Glassmorphism, Dark mode)
│   ├── js/            # Interactivity and Biometric simulation
│   └── images/        # Assets and Party Symbols
├── templates/         # HTML templates (Jinja2)
├── app.py             # Flask application & Routes
├── models.py          # Database schema & Initialization
├── requirements.txt   # Python dependencies
├── vercel.json        # Vercel deployment configuration
└── README.md          # Project documentation
```

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
