# 🌩️ HACKATHON 2026 REGISTRATION SYSTEM
## Complete Deployment Guide - Step-by-Step for Everyone

---

## 📋 TABLE OF CONTENTS

1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Windows Setup (Step-by-Step)](#windows-setup-step-by-step)
4. [Mac Setup (Step-by-Step)](#mac-setup-step-by-step)
5. [Linux Setup (Step-by-Step)](#linux-setup-step-by-step)
6. [Project File Structure](#project-file-structure)
7. [Complete Backend Code Explanation](#complete-backend-code-explanation)
8. [Complete Frontend Code Explanation](#complete-frontend-code-explanation)
9. [Database Setup & Testing](#database-setup--testing)
10. [Running the Application](#running-the-application)
11. [Troubleshooting Common Errors](#troubleshooting-common-errors)
12. [Verifying Everything Works](#verifying-everything-works)
13. [Project Walkthrough](#project-walkthrough)
14. [Future Improvements & Deployment](#future-improvements--deployment)

---

# 📌 INTRODUCTION

This is a **Complete Full-Stack Hackathon Registration System** consisting of:

- **Frontend**: HTML, CSS, JavaScript (beautiful dark UI with neon cyan theme)
- **Backend**: Python Flask (lightweight web framework)
- **Database**: MySQL (stores all registrations permanently)

**What this system does:**
- Students can register for the hackathon
- They choose their workshop category (Cybersecurity, Data Science, or AI/ML)
- They select a specific workshop from that category
- They choose a time slot
- All data is stored in MySQL database
- Admins can view all registrations in a formatted table

**By the end of this guide**, you will have a fully working hackathon registration website on your laptop that you can:
- Run locally
- Deploy to the cloud
- Modify and customize
- Show in your portfolio

---

# 🖥️ SYSTEM REQUIREMENTS

## Windows
- Windows 7 or higher (Windows 10+ recommended)
- At least 4GB RAM
- 2GB free disk space

## All Operating Systems
- Internet connection for downloading software
- Administrator/sudo access
- A text editor (VS Code recommended)

---

# 💻 WINDOWS SETUP (STEP-BY-STEP)

## PHASE 1: Install Required Software

### Step 1.1: Download and Install VS Code

**What is VS Code?**
- VS Code is a free code editor made by Microsoft
- It's where you'll write and manage your code
- It has a built-in terminal to run commands

**Installation Instructions:**

1. Go to https://code.visualstudio.com/
2. Click the **Windows** download button (it will download a `.exe` file)
3. Once downloaded, double-click the installer
4. Click **"I accept the agreement"** checkbox
5. Click **Next** several times
6. When asked "Select Additional Tasks":
   - ✅ Check **"Add to PATH"**
   - ✅ Check **"Register Code as an editor for supported file types"**
7. Click **Install**
8. Click **Finish**
9. VS Code will open automatically

**Verify Installation:**
- Open VS Code
- You should see a welcome screen
- Close it

---

### Step 1.2: Install Python

**What is Python?**
- Python is a programming language that runs your backend code
- Flask (which we use) is a Python library

**Installation Instructions:**

1. Go to https://www.python.org/downloads/
2. Click **"Download Python 3.11.x"** (or latest 3.x version)
3. This downloads a `.exe` file
4. Double-click the installer
5. **⚠️ VERY IMPORTANT:**
   - ✅ **Check the box that says "Add Python to PATH"** (this is at the BOTTOM of the installer window)
   - This allows you to use Python from anywhere
6. Click **Install Now**
7. Wait for installation to complete
8. Click **Close**

**Verify Python Installation:**

1. Open VS Code
2. Click **Terminal** menu → **New Terminal**
3. A terminal window opens at the bottom
4. Type this command and press Enter:

```bash
python --version
```

5. You should see something like: `Python 3.11.7`
6. If you see this, Python is installed ✅

**If you get "command not found":**
- You might need to use `python3` instead of `python`
- Try: `python3 --version`
- If that works, remember to use `python3` for all commands below

---

### Step 1.3: Install MySQL Server (Database)

**What is MySQL?**
- MySQL is a database system that stores all your registration data
- It's the most popular database for web applications
- Think of it as a very organized spreadsheet that can handle thousands of rows

**Installation Instructions:**

1. Go to (https://nkgacademy.com/how-to-download-mysql-and-install-command-line-client-on-windows/#google_vignette)
2. Download the **"MySQL Installer For Windows"** (usually the larger file, about 200MB)
3. Run the downloaded `.msi` file
4. Click **Next**
5. Accept the license agreement
6. Choose **Setup Type**: Select **"Custom"** (not Developer Default)
7. Click **Next**
8. Under **Products to Install**, select only:
   - MySQL Server 5.5
9. Click **Next**
10. Under **Type and Networking**, keep defaults
11. Click **Next**
12. Under **MySQL Server Configuration**:
    - **Config Type**: Development Computer
    - **TCP Port**: 3306 (default)
13. Click **Next**
14. Under **MySQL Server User Accounts**:
    - **Username**: `root`
    - **Password**: `root` (for development only! Never use this in production)
    - **Confirm Password**: `root`
    - Keep "MySQL User Accounts" as is
15. Click **Next**
16. Under **Windows Service**:
    - ✅ Check **"Configure MySQL Server as a Windows Service"**
    - Service Name: `MySQL80` (or whatever is suggested)
17. Click **Next**
18. Click **Execute** to install
19. Wait for installation to complete (this might take a few minutes)
20. Click **Finish** when complete

**Verify MySQL Installation:**

1. Open Command Prompt (or use VS Code terminal)
2. Type this command:

```bash
mysql -u root -p
```

3. Press Enter
4. When asked for password, type: `root` and press Enter
5. You should see the MySQL prompt:

```
mysql>
```

6. Type: `exit` and press Enter to close MySQL
7. If you see the `mysql>` prompt, MySQL is installed ✅

---

### Step 1.4: Install Python Libraries (Flask & MySQL Connector)

**What are these libraries?**
- **Flask**: Turns Python into a web server (handles web requests)
- **mysql-connector-python**: Allows Python to talk to MySQL database

**Installation Instructions:**

1. Open VS Code
2. Open Terminal (Terminal → New Terminal)
3. Type this command and press Enter:

```bash
pip install flask
```

4. Wait for the installation (you'll see lots of text scrolling)
5. When it's done, you should see:

```
Successfully installed flask-x.x.x ...
```

6. Now install MySQL connector:

```bash
pip install mysql-connector-python
```

7. Wait for installation
8. You should see: `Successfully installed mysql-connector-python-x.x.x`

**Verify Installations:**

1. In terminal, type:

```bash
pip list
```

2. You should see in the list:
   - `Flask` (with a version number)
   - `mysql-connector-python`

If both are there, you're good! ✅

---

## PHASE 2: Create Project Folder and Files

### Step 2.1: Create Project Folder

1. Open **File Explorer** (Windows Explorer)
2. Go to your Documents folder or Desktop
3. Right-click in empty space
4. Select **New** → **Folder**
5. Name it: `hackathon-registration`
6. Open this new folder

---

### Step 2.2: Create Files in VS Code

1. Open VS Code
2. Click **File** → **Open Folder**
3. Select your `hackathon-registration` folder
4. Click **Select Folder**
5. VS Code now shows your folder on the left side
6. Right-click in the left sidebar (under your folder name)
7. Select **New File**
8. Name it: `app.py`
9. Create another file: `index.html`
10. Create another file: `requirements.txt`

You should now have 3 files:
```
hackathon-registration/
├── app.py
├── index.html
└── requirements.txt
```

---

### Step 2.3: Add Content to requirements.txt

1. Click on `requirements.txt` in VS Code
2. Copy this text and paste it:

```
flask==2.3.3
mysql-connector-python==8.1.0
```

3. Press **Ctrl+S** to save

This file lists all Python libraries you need. Later, others can run `pip install -r requirements.txt` to install everything at once.

---

## PHASE 3: Add Code to Your Files

### Step 3.1: Add Backend Code (app.py)

1. Click on `app.py` in VS Code
2. Copy the entire backend code from Section "BACKEND CODE" below
3. Paste it into `app.py`
4. Press **Ctrl+S** to save

---

### Step 3.2: Add Frontend Code (index.html)

1. Click on `index.html` in VS Code
2. Copy the entire frontend code from Section "FRONTEND CODE" below
3. Paste it into `index.html`
4. Press **Ctrl+S** to save

---

## PHASE 4: Start MySQL Service

Before running your app, MySQL must be running.

**Option 1: Automatic (if you installed Windows Service)**

MySQL should start automatically when you restart Windows. You can verify it's running:

1. Press **Windows Key + R**
2. Type: `services.msc`
3. Press Enter
4. Look for **MySQL80** in the list
5. It should say **Running** (if not, right-click and select **Start**)

**Option 2: Manual Start (Alternative)**

1. Open Command Prompt as Administrator
2. Type:

```bash
net start MySQL80
```

3. Press Enter
4. You should see: `The MySQL80 service is starting...`
5. Wait for: `The MySQL80 service has been started successfully.`

---

## PHASE 5: Create Database (One-Time Setup)

1. Open VS Code
2. Open Terminal
3. Type this command:

```bash
mysql -u root -p
```

4. Press Enter
5. Type password: `root`
6. Press Enter
7. Now you're in MySQL. Type:

```sql
CREATE DATABASE IF NOT EXISTS hackathon_db;
```

8. Press Enter
9. You should see: `Query OK, 1 row affected`
10. Now type:

```sql
USE hackathon_db;
```

11. Press Enter
12. Type:

```sql
CREATE TABLE IF NOT EXISTS registrations (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    full_name  VARCHAR(255)  NOT NULL,
    email      VARCHAR(255)  NOT NULL UNIQUE,
    university VARCHAR(255)  NOT NULL,
    workshops  VARCHAR(255)  NOT NULL,
    category   VARCHAR(100)  NOT NULL,
    timeslot   VARCHAR(100)  NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

13. Press Enter
14. You should see: `Query OK, 0 rows affected`
15. Type: `exit`
16. Press Enter

✅ Your database is now created!

---

## PHASE 6: Run Your Application

1. Open VS Code
2. Make sure you're in your project folder (you should see `app.py`, `index.html` in left sidebar)
3. Open Terminal (Terminal → New Terminal)
4. Type:

```bash
python app.py
```

5. Press Enter
6. You should see output like:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

7. Open your web browser (Chrome, Firefox, Edge, etc.)
8. Go to: `http://localhost:5000`
9. You should see the Hackathon Registration website! 🎉

**Keep this terminal open** - if you close it, the app stop

# 📁 PROJECT FILE STRUCTURE

Once everything is set up, your folder should look like:

```
hackathon-registration/
│
├── app.py                    ← Flask backend (Python)
├── index.html                ← Frontend (HTML/CSS/JavaScript)
├── requirements.txt          ← Python dependencies
└── README.md                 ← Documentation (optional)
```

**That's it!** No complex folder structure needed.

The database files are stored by MySQL (automatically in MySQL data directory):
- Windows: `C:\ProgramData\MySQL\MySQL Server 8.0\Data\`
- Mac: `/usr/local/var/mysql/`
- Linux: `/var/lib/mysql/`

---

---

# 🧠 COMPLETE BACKEND CODE EXPLANATION

## Full Backend Code (app.py)

```python
from flask import Flask, request, send_from_directory
import mysql.connector
import os

# ═══════════════════════════════════════════════════════════════
#  CREATE FLASK APPLICATION
# ═══════════════════════════════════════════════════════════════

app = Flask(__name__)

# ═══════════════════════════════════════════════════════════════
#  DATABASE CONFIGURATION
# ═══════════════════════════════════════════════════════════════

DB_CONFIG = {
    "host": "localhost",          # Where MySQL is running (local computer)
    "user": "root",               # MySQL username
    "password": "root",           # MySQL password (change in production!)
    "database": "hackathon_db"    # Name of our database
}

# ═══════════════════════════════════════════════════════════════
#  HELPER FUNCTION: Create Database Connection
# ═══════════════════════════════════════════════════════════════

def get_db():
    """
    Creates and returns a fresh MySQL connection.
    
    Why do we need this?
    - Each time we need to query the database, we create a new connection
    - This keeps the code clean and prevents connection leaks
    - Alternative: We could create one connection and reuse it, but that's
      more complex to manage
    
    Returns:
        mysql.connector.connection.MySQLConnection: A database connection object
    """
    return mysql.connector.connect(**DB_CONFIG)
    # **DB_CONFIG unpacks the dictionary into function arguments
    # Equivalent to: mysql.connector.connect(host="localhost", user="root", ...)


# ═══════════════════════════════════════════════════════════════
#  HELPER FUNCTION: Initialize Database & Table
# ═══════════════════════════════════════════════════════════════

def init_db():
    """
    Creates the database and table if they don't exist.
    
    This runs ONCE when you first start the app.
    
    Steps:
    1. Connect to MySQL (without selecting a database)
    2. Create the database if it doesn't exist
    3. Select that database
    4. Create the registrations table with proper columns
    5. Close connection
    
    Table Columns:
    - id: Unique number for each registration (auto-incremented)
    - full_name: Student's name
    - email: Student's email (must be unique)
    - university: Which college they're from
    - workshops: Which workshop they chose
    - category: Which category (Cybersecurity, Data Science, AI/ML)
    - timeslot: Which time slot (Morning, Afternoon, Evening)
    - created_at: Timestamp when they registered
    """
    
    # Connect to MySQL without specifying a database
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cur = conn.cursor()
    
    # Create database if it doesn't exist
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    
    # Now select that database
    cur.execute(f"USE {DB_CONFIG['database']}")
    
    # Create the registrations table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id         INT AUTO_INCREMENT PRIMARY KEY,
            full_name  VARCHAR(255)  NOT NULL,
            email      VARCHAR(255)  NOT NULL UNIQUE,
            university VARCHAR(255)  NOT NULL,
            workshops  VARCHAR(255)  NOT NULL,
            category   VARCHAR(100)  NOT NULL,
            timeslot   VARCHAR(100)  NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Save all changes
    conn.commit()
    
    # Close cursor and connection
    cur.close()
    conn.close()
    
    print("✅ Database & table ready.")


# ═══════════════════════════════════════════════════════════════
#  ROUTE 1: Serve the Website
# ═══════════════════════════════════════════════════════════════

@app.route("/")
def index():
    """
    Serves the HTML file (index.html).
    
    When someone goes to http://localhost:5000/, this function runs.
    It finds index.html in the same folder as app.py and sends it to the browser.
    
    The @app.route("/") decorator means:
    - "/" is the root URL (home page)
    - This function handles that URL
    """
    return send_from_directory(os.path.dirname(__file__), "index.html")


# ═══════════════════════════════════════════════════════════════
#  ROUTE 2: Register a Student (POST Request)
# ═══════════════════════════════════════════════════════════════

@app.route("/api/register", methods=["POST"])
def register():
    """
    Handles registration form submission.
    
    When someone fills out the form and clicks "Submit", JavaScript sends
    the data to this endpoint as a POST request.
    
    Steps:
    1. Get form data from the request
    2. Validate that all fields are filled
    3. Insert data into the database
    4. Return success or error message
    
    Error Handling:
    - If email already exists: Return 409 (Conflict)
    - If database error: Return 500 (Server Error)
    - If missing fields: Return 400 (Bad Request)
    - If success: Return 201 (Created)
    """
    
    # Get form data from JavaScript fetch() call
    full_name  = request.form.get("fullName", "").strip()
    email      = request.form.get("email", "").strip()
    university = request.form.get("university", "").strip()
    category   = request.form.get("category", "").strip()
    workshops  = request.form.get("workshops", "").strip()
    timeslot   = request.form.get("timeslot", "").strip()
    
    # Validate that required fields are not empty
    if not all([full_name, email, university, category, workshops, timeslot]):
        return "All fields are required.", 400
    
    # Try to insert into database
    try:
        conn = get_db()
        cur = conn.cursor()
        
        cur.execute("""
            INSERT INTO registrations 
            (full_name, email, university, category, workshops, timeslot)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (full_name, email, university, category, workshops, timeslot))
        
        conn.commit()
        cur.close()
        conn.close()
        
        return "Registration successful.", 201
    
    # Handle duplicate email error
    except mysql.connector.errors.IntegrityError:
        return "This email is already registered.", 409
    
    # Handle any other database error
    except Exception as e:
        print(f"DB error: {e}")
        return "Server error. Please try again.", 500


# ═══════════════════════════════════════════════════════════════
#  ROUTE 3: View All Registrations (GET Request)
# ═══════════════════════════════════════════════════════════════

@app.route("/api/registrations", methods=["GET"])
def view_registrations():
    """
    Returns all registrations as an HTML table.
    
    When someone clicks "View Registrations" button, JavaScript calls this.
    We fetch data from database and format it as an HTML table with styling.
    
    Returns:
    - HTML table with all registrations
    - Styled with cyan/dark theme to match frontend
    """
    
    try:
        conn = get_db()
        cur = conn.cursor(dictionary=True)  # dictionary=True means rows are dictionaries
        
        # Get all registrations, newest first
        cur.execute("SELECT * FROM registrations ORDER BY created_at DESC")
        rows = cur.fetchall()
        
        cur.close()
        conn.close()
    
    except Exception as e:
        print(f"DB error: {e}")
        return "<p style='color:#f00'>Could not load registrations.</p>", 500
    
    # If no registrations yet
    if not rows:
        return "<p style='color:#0af;text-align:center;padding:20px'>No registrations yet.</p>"
    
    # Build HTML table
    html = """
    <style>
        .reg-table { 
            width: 100%; 
            border-collapse: collapse; 
            font-size: 13px; 
        }
        .reg-table th {
            background: rgba(0, 255, 255, 0.15); 
            color: #0ff;
            padding: 10px 14px; 
            text-align: left;
            text-transform: uppercase; 
            letter-spacing: 1px;
            border-bottom: 2px solid #0ff;
        }
        .reg-table td {
            color: #0af; 
            padding: 10px 14px;
            border-bottom: 1px solid rgba(0, 255, 255, 0.15);
        }
        .reg-table tr:hover td { 
            background: rgba(0, 255, 255, 0.05); 
        }
        .badge {
            display: inline-block; 
            padding: 3px 8px;
            background: rgba(0, 255, 255, 0.1); 
            border: 1px solid #0ff;
            border-radius: 3px; 
            font-size: 11px; 
            margin: 2px 2px 2px 0;
        }
    </style>
    <table class="reg-table">
      <thead>
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Email</th>
          <th>University</th>
          <th>Category</th>
          <th>Workshop</th>
          <th>Time Slot</th>
          <th>Registered At</th>
        </tr>
      </thead>
      <tbody>
    """
    
    # Add each registration as a table row
    for i, r in enumerate(rows, 1):
        # Format the workshop as a badge
        workshop_badge = f'<span class="badge">{r["workshops"]}</span>'
        category_badge = f'<span class="badge">{r["category"]}</span>'
        
        # Format the timestamp
        created_at = r['created_at'].strftime('%b %d, %Y  %H:%M') if r['created_at'] else 'N/A'
        
        html += f"""
        <tr>
          <td>{i}</td>
          <td>{r['full_name']}</td>
          <td>{r['email']}</td>
          <td>{r['university']}</td>
          <td>{category_badge}</td>
          <td>{workshop_badge}</td>
          <td>{r['timeslot']}</td>
          <td>{created_at}</td>
        </tr>"""
    
    html += "</tbody></table>"
    return html


# ═══════════════════════════════════════════════════════════════
#  ERROR HANDLERS (Optional)
# ═══════════════════════════════════════════════════════════════

@app.errorhandler(404)
def not_found(error):
    """Handle page not found errors"""
    return "<h1>404 - Page Not Found</h1>", 404


@app.errorhandler(500)
def server_error(error):
    """Handle server errors"""
    return "<h1>500 - Server Error</h1>", 500


# ═══════════════════════════════════════════════════════════════
#  MAIN ENTRY POINT - Runs when you execute: python app.py
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Create database and table (happens automatically)
    init_db()
    
    # Start the Flask server
    # debug=True means the server automatically reloads when you change code
    # port=5000 is the server port (you'll access it at http://localhost:5000)
    app.run(debug=True, port=5000)
    
    # When you press Ctrl+C, the server stops
```

---

## Backend Code - Line-by-Line Breakdown

### Import Section
```python
from flask import Flask, request, send_from_directory
import mysql.connector
import os
```

**What each import does:**
- `Flask`: Creates web server
- `request`: Gets data from form submissions
- `send_from_directory`: Serves HTML/CSS/JS files
- `mysql.connector`: Connects Python to MySQL
- `os`: Handles file paths (cross-platform)

### Database Configuration
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "hackathon_db"
}
```

**Explanation:**
- All database settings in one place
- Easy to change for production

### HTTP Status Codes Used
- `201`: Created (registration successful)
- `400`: Bad Request (missing fields)
- `409`: Conflict (email already exists)
- `500`: Server Error (database error)

---

---

# 🎨 COMPLETE FRONTEND CODE EXPLANATION

## Full Frontend Code (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hackathon 2026 - Registration</title>
    <style>
        /* ═══════════════════════════════════════════════════════════ */
        /*                      GLOBAL STYLES                         */
        /* ═══════════════════════════════════════════════════════════ */
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%);
            color: #0ff;
            min-height: 100vh;
            padding: 20px;
        }
        
        .wrapper {
            max-width: 900px;
            margin: 0 auto;
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      NAVIGATION BAR                         */
        /* ═══════════════════════════════════════════════════════════ */
        
        .nav-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 2px solid #0ff;
            animation: slideDown 0.8s ease-out;
        }
        
        @keyframes slideDown {
            from {
                transform: translateY(-50px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
            text-shadow: 0 0 20px #0ff;
            letter-spacing: 3px;
        }
        
        .nav-buttons {
            display: flex;
            gap: 15px;
        }
        
        .nav-btn {
            background: transparent;
            border: 2px solid #0ff;
            color: #0ff;
            padding: 8px 20px;
            cursor: pointer;
            font-family: inherit;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-radius: 3px;
            transition: all 0.3s ease;
        }
        
        .nav-btn:hover,
        .nav-btn.active {
            background: #0ff;
            color: #0f1419;
            box-shadow: 0 0 15px #0ff;
            transform: translateY(-2px);
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      PAGE SWITCHING                         */
        /* ═══════════════════════════════════════════════════════════ */
        
        .page {
            display: none;
            animation: fadeIn 0.8s ease-out;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .page.active {
            display: block;
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      PAGE TITLES                            */
        /* ═══════════════════════════════════════════════════════════ */
        
        .page-title {
            font-size: 32px;
            margin-bottom: 30px;
            text-shadow: 0 0 20px #0ff;
            letter-spacing: 2px;
            animation: glow 3s ease-in-out infinite;
        }
        
        @keyframes glow {
            0%,
            100% {
                text-shadow: 0 0 10px #0ff;
            }
            50% {
                text-shadow: 0 0 30px #0ff, 0 0 40px #00ffff;
            }
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      CARDS & CONTAINERS                     */
        /* ═══════════════════════════════════════════════════════════ */
        
        .event-card {
            background: rgba(26, 31, 46, 0.9);
            border: 2px solid #0ff;
            border-radius: 5px;
            padding: 25px;
            margin-bottom: 20px;
            animation: slideUp 0.7s ease-out;
        }
        
        @keyframes slideUp {
            from {
                transform: translateY(30px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }
        
        .event-card h2 {
            color: #0ff;
            font-size: 20px;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .event-card p {
            color: #0af;
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 15px;
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      INFO GRID                              */
        /* ═══════════════════════════════════════════════════════════ */
        
        .info-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 15px 0;
            font-size: 13px;
        }
        
        .info-item {
            background: rgba(15, 20, 25, 0.8);
            padding: 12px;
            border-left: 3px solid #0ff;
            border-radius: 2px;
        }
        
        .info-label {
            color: #0ff;
            font-weight: bold;
            text-transform: uppercase;
            font-size: 11px;
            margin-bottom: 5px;
        }
        
        .info-value {
            color: #0af;
            font-size: 14px;
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      BUTTONS                                */
        /* ═══════════════════════════════════════════════════════════ */
        
        .cta-button {
            background: #0ff;
            color: #0f1419;
            border: none;
            padding: 12px 30px;
            font-size: 14px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            cursor: pointer;
            border-radius: 3px;
            margin-top: 15px;
            transition: all 0.3s ease;
            font-family: inherit;
        }
        
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 0 20px #0ff;
        }
        
        .submit-btn {
            background: #0ff;
            color: #0f1419;
            border: none;
            padding: 14px 40px;
            font-size: 15px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            cursor: pointer;
            border-radius: 3px;
            width: 100%;
            margin-top: 20px;
            transition: all 0.3s ease;
            font-family: inherit;
        }
        
        .submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 25px #0ff;
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      FORMS                                  */
        /* ═══════════════════════════════════════════════════════════ */
        
        .form-section {
            animation: slideUp 0.7s ease-out;
        }
        
        .form-group {
            margin-bottom: 20px;
            animation: slideUp 0.7s ease-out;
        }
        
        label {
            display: block;
            color: #0ff;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
            font-weight: bold;
        }
        
        input,
        select,
        textarea {
            width: 100%;
            padding: 12px;
            background: rgba(15, 20, 25, 0.9);
            border: 2px solid #0ff;
            color: #0ff;
            font-family: inherit;
            font-size: 14px;
            border-radius: 3px;
            transition: all 0.3s ease;
        }
        
        input:focus,
        select:focus,
        textarea:focus {
            outline: none;
            box-shadow: 0 0 15px #0ff;
            background: rgba(0, 255, 255, 0.05);
            border-color: #00ffff;
        }
        
        select option {
            background: #0f1419;
            color: #0ff;
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      WORKSHOP CARDS                         */
        /* ═══════════════════════════════════════════════════════════ */
        
        .workshop-cards {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-top: 8px;
        }
        
        .workshop-card {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 14px 16px;
            background: rgba(15, 20, 25, 0.8);
            border-radius: 3px;
            border: 1px solid #0ff;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .workshop-card:hover {
            background: rgba(0, 255, 255, 0.08);
            box-shadow: 0 0 10px #0ff;
        }
        
        .workshop-card input[type="radio"] {
            width: auto;
            margin: 0;
            cursor: pointer;
            accent-color: #0ff;
        }
        
        .workshop-card label {
            margin: 0;
            cursor: pointer;
            flex: 1;
            font-size: 14px;
            text-transform: none;
            letter-spacing: 0;
            font-weight: normal;
        }
        
        .workshop-badge {
            font-size: 10px;
            background: rgba(0, 255, 255, 0.1);
            border: 1px solid #0ff;
            color: #0ff;
            padding: 2px 8px;
            border-radius: 2px;
            text-transform: uppercase;
            letter-spacing: 1px;
            white-space: nowrap;
        }
        
        .workshops-hidden {
            display: none;
        }
        
        .category-hint {
            font-size: 12px;
            color: #0af;
            margin-top: 8px;
            padding: 8px 12px;
            background: rgba(0, 255, 255, 0.05);
            border-left: 2px solid #0af;
            border-radius: 2px;
            display: none;
        }
        
        .category-hint.show {
            display: block;
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      SCHEDULE                               */
        /* ═══════════════════════════════════════════════════════════ */
        
        .day-schedule {
            background: rgba(15, 20, 25, 0.8);
            border: 2px solid #0ff;
            padding: 15px;
            border-radius: 3px;
            margin-bottom: 15px;
        }
        
        .day-schedule h3 {
            color: #0ff;
            font-size: 16px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        
        .schedule-item {
            color: #0af;
            font-size: 13px;
            padding: 8px 0;
            border-bottom: 1px solid rgba(0, 255, 255, 0.2);
        }
        
        .schedule-item:last-child {
            border-bottom: none;
        }
        
        .time {
            color: #0ff;
            font-weight: bold;
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      ALERTS                                 */
        /* ═══════════════════════════════════════════════════════════ */
        
        .alert {
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 3px;
            border-left: 4px solid;
            display: none;
        }
        
        .alert.success {
            background: rgba(0, 255, 100, 0.1);
            border-color: #0f0;
            color: #0f0;
            display: block;
        }
        
        .alert.error {
            background: rgba(255, 0, 100, 0.1);
            border-color: #f00;
            color: #f00;
            display: block;
        }
        
        /* ═══════════════════════════════════════════════════════════ */
        /*                      POPUPS                                 */
        /* ═══════════════════════════════════════════════════════════ */
        
        .popup {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.8);
            justify-content: center;
            align-items: center;
            z-index: 1000;
            animation: fadeIn 0.3s ease-out;
        }
        
        .popup.show {
            display: flex;
        }
        
        .popup-content {
            background: #0f1419;
            border: 3px solid #0ff;
            padding: 30px;
            border-radius: 5px;
            text-align: center;
            max-width: 400px;
            box-shadow: 0 0 30px #0ff;
            animation: popupScale 0.4s ease-out;
        }
        
        @keyframes popupScale {
            from {
                transform: scale(0.8);
                opacity: 0;
            }
            to {
                transform: scale(1);
                opacity: 1;
            }
        }
        
        .popup-content h2 {
            color: #0ff;
            font-size: 24px;
            margin-bottom: 15px;
            text-shadow: 0 0 20px #0ff;
            letter-spacing: 2px;
        }
        
        .popup-content p {
            color: #0af;
            font-size: 14px;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        
        .popup-btn {
            background: #0ff;
            color: #0f1419;
            border: none;
            padding: 10px 25px;
            font-size: 13px;
            font-weight: bold;
            cursor: pointer;
            border-radius: 3px;
            transition: all 0.3s ease;
            font-family: inherit;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .popup-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 15px #0ff;
        }
    </style>
</head>
<body>
    <div class="wrapper">
        <!-- ═══════════════════════════════════════════════════════════ -->
        <!--                   NAVIGATION BAR                           -->
        <!-- ═══════════════════════════════════════════════════════════ -->
        
        <div class="nav-bar">
            <div class="logo">&gt; EVENT.HUB</div>
            <div class="nav-buttons">
                <button class="nav-btn active" onclick="showPage('home')">Home</button>
                <button class="nav-btn" onclick="showPage('register')">Register</button>
                <button class="nav-btn" onclick="showPage('view')">View Registrations</button>
            </div>
        </div>

        <!-- ═══════════════════════════════════════════════════════════ -->
        <!--                   HOME PAGE                                -->
        <!-- ═══════════════════════════════════════════════════════════ -->

        <div id="home" class="page active">
            <div class="page-title">HACKATHON 2026</div>
            
            <div class="event-card">
                <h2>Welcome to the Ultimate Coding Challenge</h2>
                <p>Join hundreds of students for an intense 2-day hackathon experience. Build, compete, and showcase your skills!</p>
            </div>
            
            <div class="event-card">
                <h2>Event Details</h2>
                <div class="info-row">
                    <div class="info-item">
                        <div class="info-label">Dates</div>
                        <div class="info-value">March 22-23, 2026</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Location</div>
                        <div class="info-value">Tech Campus - Hall A</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Duration</div>
                        <div class="info-value">48 Hours Non-Stop</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Level</div>
                        <div class="info-value">Beginner Friendly</div>
                    </div>
                </div>
            </div>
            
            <div class="event-card">
                <h2>What's Included</h2>
                <div class="day-schedule">
                    <h3>Day 1: Foundations</h3>
                    <div class="schedule-item"><span class="time">9:00 AM</span> - Opening Ceremony</div>
                    <div class="schedule-item"><span class="time">10:00 AM</span> - Team Formation</div>
                    <div class="schedule-item"><span class="time">12:00 PM</span> - Lunch Break</div>
                    <div class="schedule-item"><span class="time">1:00 PM</span> - Hacking Begins</div>
                    <div class="schedule-item"><span class="time">7:00 PM</span> - Dinner & Networking</div>
                </div>
                <div class="day-schedule">
                    <h3>Day 2: Creation & Showcase</h3>
                    <div class="schedule-item"><span class="time">8:00 AM</span> - Breakfast & Coding</div>
                    <div class="schedule-item"><span class="time">12:00 PM</span> - Final Lunch</div>
                    <div class="schedule-item"><span class="time">2:00 PM</span> - Submission Deadline</div>
                    <div class="schedule-item"><span class="time">3:00 PM</span> - Project Showcase</div>
                    <div class="schedule-item"><span class="time">5:00 PM</span> - Awards & Closing</div>
                </div>
            </div>
            
            <div class="event-card">
                <h2>Amazing Prizes</h2>
                <p>Prize pool worth $5000+ distributed among top performers. Internship opportunities with leading tech companies. Networking with industry professionals. Free merchandise and certificates!</p>
                <button class="cta-button" onclick="showPage('register')">Register Now</button>
            </div>
        </div>

        <!-- ═══════════════════════════════════════════════════════════ -->
        <!--                   REGISTER PAGE                            -->
        <!-- ═══════════════════════════════════════════════════════════ -->

        <div id="register" class="page">
            <div class="page-title">STUDENT REGISTRATION</div>
            <div class="event-card">
                <h2>Register for Hackathon 2026</h2>
                <p>Complete the form below to secure your spot at the event. Limited seats available!</p>

                <div id="alertMessage" class="alert"></div>

                <form id="registrationForm">
                    <div class="form-section">
                        <div class="form-group">
                            <label>Full Name *</label>
                            <input type="text" id="fullName" name="fullName" placeholder="Enter your full name" required>
                        </div>
                        
                        <div class="form-group">
                            <label>Email Address *</label>
                            <input type="email" id="email" name="email" placeholder="student@college.edu" required>
                        </div>
                        
                        <div class="form-group">
                            <label>University / College *</label>
                            <input type="text" id="university" name="university" placeholder="Your college name" required>
                        </div>

                        <!-- STEP 1: Choose Category -->
                        <div class="form-group">
                            <label>Workshop Category *</label>
                            <select id="workshopCategory" onchange="showWorkshops(this.value)">
                                <option value="">-- Select a Category --</option>
                                <option value="cyber">Cybersecurity</option>
                                <option value="datascience">Data Science</option>
                                <option value="aiml">AI / Machine Learning</option>
                            </select>
                            <div class="category-hint" id="categoryHint">
                                Choose one workshop from this category to attend.
                            </div>
                        </div>

                        <!-- STEP 2: Choose Workshop from Category -->
                        <div class="form-group workshops-hidden" id="workshopSection">
                            <label>Select Workshop *</label>

                            <!-- Cybersecurity workshops -->
                            <div class="workshop-cards" id="workshops-cyber" style="display:none">
                                <div class="workshop-card">
                                    <input type="radio" name="workshop" value="Ethical Hacking" id="w1">
                                    <label for="w1">Ethical Hacking & Penetration Testing</label>
                                    <span class="workshop-badge">Cyber</span>
                                </div>
                                <div class="workshop-card">
                                    <input type="radio" name="workshop" value="Network Security" id="w2">
                                    <label for="w2">Network Security & Threat Analysis</label>
                                    <span class="workshop-badge">Cyber</span>
                                </div>
                            </div>

                            <!-- Data Science workshops -->
                            <div class="workshop-cards" id="workshops-datascience" style="display:none">
                                <div class="workshop-card">
                                    <input type="radio" name="workshop" value="Data Visualization" id="w3">
                                    <label for="w3">Data Visualization & Analytics</label>
                                    <span class="workshop-badge">Data Sci</span>
                                </div>
                                <div class="workshop-card">
                                    <input type="radio" name="workshop" value="Big Data Engineering" id="w4">
                                    <label for="w4">Big Data Engineering with Python</label>
                                    <span class="workshop-badge">Data Sci</span>
                                </div>
                            </div>

                            <!-- AI / ML workshops -->
                            <div class="workshop-cards" id="workshops-aiml" style="display:none">
                                <div class="workshop-card">
                                    <input type="radio" name="workshop" value="Deep Learning" id="w5">
                                    <label for="w5">Deep Learning & Neural Networks</label>
                                    <span class="workshop-badge">AI / ML</span>
                                </div>
                                <div class="workshop-card">
                                    <input type="radio" name="workshop" value="NLP Fundamentals" id="w6">
                                    <label for="w6">NLP & Large Language Models</label>
                                    <span class="workshop-badge">AI / ML</span>
                                </div>
                            </div>
                        </div>

                        <div class="form-group">
                            <label>Select Time Slot *</label>
                            <select id="timeslot" name="timeslot" required>
                                <option value="">-- Select Slot --</option>
                                <option value="Morning">10:00 AM - 12:00 PM</option>
                                <option value="Afternoon">1:00 PM - 3:00 PM</option>
                                <option value="Evening">4:00 PM - 6:00 PM</option>
                            </select>
                        </div>

                        <button type="submit" class="submit-btn">SUBMIT REGISTRATION</button>
                    </div>
                </form>
            </div>
        </div>

        <!-- ═══════════════════════════════════════════════════════════ -->
        <!--                   VIEW REGISTRATIONS PAGE                  -->
        <!-- ═══════════════════════════════════════════════════════════ -->

        <div id="view" class="page">
            <div class="page-title">VIEW REGISTRATIONS</div>
            <div class="event-card">
                <h2>All Registered Students</h2>
                <div id="registrationsList"></div>
            </div>
        </div>
    </div>

    <!-- ═══════════════════════════════════════════════════════════ -->
    <!--                   SUCCESS POPUP                            -->
    <!-- ═══════════════════════════════════════════════════════════ -->

    <div id="successPopup" class="popup">
        <div class="popup-content">
            <h2>Registration Complete!</h2>
            <p>Welcome to Hackathon 2026! Check your email for confirmation details and further instructions.</p>
            <p>Event Date: March 22-23, 2026</p>
            <p>See you at the event!</p>
            <button class="popup-btn" onclick="closePopup()">Close</button>
        </div>
    </div>

    <script>
        // ═══════════════════════════════════════════════════════════════
        //                    PAGE NAVIGATION FUNCTION
        // ═══════════════════════════════════════════════════════════════
        
        function showPage(pageName) {
            /**
             * Switches between pages (Home, Register, View)
             * 
             * Process:
             * 1. Hide all pages
             * 2. Deactivate all nav buttons
             * 3. Show the selected page
             * 4. Activate the corresponding button
             * 5. Load registrations if viewing that page
             * 6. Scroll to top
             */
            
            const pages = document.querySelectorAll('.page');
            const navBtns = document.querySelectorAll('.nav-btn');
            
            // Hide all pages
            pages.forEach(p => p.classList.remove('active'));
            
            // Deactivate all buttons
            navBtns.forEach(b => b.classList.remove('active'));
            
            // Show selected page
            document.getElementById(pageName).classList.add('active');
            
            // Activate the button
            event.target.classList.add('active');
            
            // Load registrations if viewing
            if (pageName === 'view') {
                loadRegistrations();
            }
            
            // Scroll to top
            window.scrollTo(0, 0);
        }

        // ═══════════════════════════════════════════════════════════════
        //                    WORKSHOP SELECTOR FUNCTION
        // ═══════════════════════════════════════════════════════════════
        
        function showWorkshops(category) {
            /**
             * Shows/hides workshop options based on selected category
             * 
             * When user selects a category:
             * 1. Hide all workshop groups
             * 2. Clear any previously selected workshop
             * 3. Show only the workshops for that category
             * 4. Show the workshop selection section
             * 5. Update the hint text
             */
            
            // Hide all workshop groups
            ['cyber', 'datascience', 'aiml'].forEach(c => {
                document.getElementById('workshops-' + c).style.display = 'none';
            });
            
            // Clear previously selected workshop
            document.querySelectorAll('input[name="workshop"]').forEach(r => r.checked = false);

            const section = document.getElementById('workshopSection');
            const hint = document.getElementById('categoryHint');

            // If no category selected
            if (!category) {
                section.style.display = 'none';
                hint.classList.remove('show');
                return;
            }

            // Show the selected category's workshops
            document.getElementById('workshops-' + category).style.display = 'flex';
            section.style.display = 'block';
            hint.classList.add('show');

            // Update hint text
            const labels = {
                cyber: 'Cybersecurity — choose 1 of 2 workshops below.',
                datascience: 'Data Science — choose 1 of 2 workshops below.',
                aiml: 'AI / Machine Learning — choose 1 of 2 workshops below.'
            };
            hint.textContent = labels[category];
        }

        // ═══════════════════════════════════════════════════════════════
        //                    ALERT MESSAGE FUNCTION
        // ═══════════════════════════════════════════════════════════════
        
        function showAlert(message, type) {
            /**
             * Display error or success message
             * 
             * Parameters:
             * - message: Text to display
             * - type: 'error' (red) or 'success' (green)
             * 
             * Alert automatically hides after 5 seconds
             */
            
            const alertDiv = document.getElementById('alertMessage');
            alertDiv.textContent = message;
            alertDiv.className = `alert ${type}`;
            
            // Auto-hide after 5 seconds
            setTimeout(() => {
                alertDiv.className = 'alert';
            }, 5000);
        }

        // ═══════════════════════════════════════════════════════════════
        //                    POPUP FUNCTIONS
        // ═══════════════════════════════════════════════════════════════
        
        function closePopup() {
            /**
             * Close success popup and return to home page
             */
            document.getElementById('successPopup').classList.remove('show');
            showPage('home');
        }

        // ═══════════════════════════════════════════════════════════════
        //                    FORM SUBMISSION HANDLER
        // ═══════════════════════════════════════════════════════════════
        
        document.getElementById('registrationForm').addEventListener('submit', async function(e) {
            /**
             * Handles registration form submission
             * 
             * Steps:
             * 1. Prevent default form submission
             * 2. Validate that category and workshop are selected
             * 3. Prepare form data
             * 4. Send to backend via fetch() POST request
             * 5. Handle success or error response
             */
            
            e.preventDefault(); // Don't reload page

            // Validate category selection
            const category = document.getElementById('workshopCategory').value;
            if (!category) {
                showAlert('Please select a workshop category.', 'error');
                return;
            }

            // Validate workshop selection
            const selectedWorkshop = document.querySelector('input[name="workshop"]:checked');
            if (!selectedWorkshop) {
                showAlert('Please select a workshop from the category.', 'error');
                return;
            }

            // Prepare data to send
            const params = new URLSearchParams({
                fullName: document.getElementById('fullName').value,
                email: document.getElementById('email').value,
                university: document.getElementById('university').value,
                workshops: selectedWorkshop.value,
                category: category,
                timeslot: document.getElementById('timeslot').value
            });

            try {
                // Send to backend
                const res = await fetch('/api/register', {
                    method: 'POST',
                    body: params
                });
                
                const text = await res.text();
                
                // Success!
                if (res.status === 201) {
                    // Reset form
                    document.getElementById('registrationForm').reset();
                    showWorkshops('');
                    document.getElementById('workshopCategory').value = '';
                    
                    // Show success popup
                    document.getElementById('successPopup').classList.add('show');
                } else {
                    // Error from backend
                    showAlert(text, 'error');
                }
            } catch (err) {
                // Network error
                showAlert('Server error. Please try again.', 'error');
            }
        });

        // ═══════════════════════════════════════════════════════════════
        //                    LOAD REGISTRATIONS FUNCTION
        // ═══════════════════════════════════════════════════════════════
        
        async function loadRegistrations() {
            /**
             * Fetches all registrations from backend and displays as table
             * 
             * Called when user clicks "View Registrations" page
             */
            
            const div = document.getElementById('registrationsList');
            
            try {
                // Fetch from backend
                const res = await fetch('/api/registrations');
                
                // Convert response to HTML
                const html = await res.text();
                
                // Display in page
                div.innerHTML = html;
            } catch (err) {
                // Show error if fetch fails
                div.innerHTML = "<p style='color:#f00'>Cannot load registrations.</p>";
            }
        }
    </script>
</body>
</html>
```

---

## Frontend Code Breakdown

### Key JavaScript Functions

**1. showPage(pageName)**
- Handles navigation between pages
- Updates active button and shows/hides pages

**2. showWorkshops(category)**
- Dynamically shows workshop options based on category
- Clears previous selections
- Updates hint text

**3. Form Submission**
- Validates all fields
- Sends data to backend via `fetch()`
- Shows success popup or error alert

**4. loadRegistrations()**
- Fetches registration table from backend
- Displays formatted HTML table

---

---

# 🗄️ DATABASE SETUP & TESTING

## What You've Already Done

When you run `app.py`, the `init_db()` function automatically:
1. Creates the `hackathon_db` database
2. Creates the `registrations` table
3. Sets up all columns properly

## Verify Database Was Created

1. Open terminal/command prompt
2. Type:

```bash
mysql -u root -p
```

3. Enter password: `root`
4. Type:

```sql
SHOW DATABASES;
```

5. You should see `hackathon_db` in the list

## View Table Structure

```sql
USE hackathon_db;
DESCRIBE registrations;
```

You should see:
```
| Field      | Type         | Null | Key | Default | Extra          |
|------------|------------|------|-----|---------|-----------------|
| id         | int        | NO   | PRI | NULL    | auto_increment  |
| full_name  | varchar    | NO   |     | NULL    |                 |
| email      | varchar    | NO   | UNI | NULL    |                 |
| university | varchar    | NO   |     | NULL    |                 |
| workshops  | varchar    | NO   |     | NULL    |                 |
| category   | varchar    | NO   |     | NULL    |                 |
| timeslot   | varchar    | NO   |     | NULL    |                 |
| created_at | timestamp  | NO   |     | CURRENT | on update      |
```

## View All Data

```sql
SELECT * FROM registrations;
```

## Delete All Test Data (if needed)

```sql
DELETE FROM registrations;
```

## Exit MySQL

```sql
exit
```

---

---

# ▶️ RUNNING THE APPLICATION

## Step-by-Step to Start

### Windows

1. Open VS Code
2. Open your project folder
3. Open Terminal (Terminal → New Terminal)
4. Make sure MySQL is running (check Services if unsure)
5. Type:

```bash
python app.py
```

6. You should see:

```
 * Running on http://127.0.0.1:5000
```

7. Open browser and go to: `http://localhost:5000`

### Mac/Linux

Same as Windows, but use `python3` if needed:

```bash
python3 app.py
```

## Testing the App

### Test 1: Home Page
- You should see "HACKATHON 2026" title
- Navigation buttons work
- Event details visible

### Test 2: Register
- Click Register button
- Fill in form:
  - Name: John Doe
  - Email: john@example.com
  - University: Tech College
  - Category: Cybersecurity
  - Workshop: Ethical Hacking
  - Time Slot: Morning
- Click Submit
- Success popup appears

### Test 3: View Registrations
- Click View Registrations
- You should see your registration in a table
- Click Register again with different email
- Check View page again - new registration appears

---

---

# ⚠️ TROUBLESHOOTING COMMON ERRORS

## Error 1: "ModuleNotFoundError: No module named 'flask'"

**Cause**: Flask not installed

**Solution**:
```bash
pip install flask
```

---

## Error 2: "ModuleNotFoundError: No module named 'mysql'"

**Cause**: MySQL connector not installed

**Solution**:
```bash
pip install mysql-connector-python
```

---

## Error 3: "Can't connect to MySQL server"

**Cause**: MySQL not running

**Solution Windows**:
```bash
net start MySQL80
```

**Solution Mac**:
```bash
mysql.server start
```

**Solution Linux**:
```bash
sudo systemctl start mysql
```

---

## Error 4: "1045 - Access denied for user 'root'"

**Cause**: Wrong password

**Solution**: 
- Check if you entered `root` as password during setup
- Reset MySQL password if needed

---

## Error 5: "Address already in use"

**Cause**: Port 5000 already used by another app

**Solution**: Change port in `app.py`:
```python
app.run(debug=True, port=5001)  # Change to 5001
```

Then access: `http://localhost:5001`

---

## Error 6: "IntegrityError: Duplicate entry"

**Cause**: Tried to register with same email twice

**Solution**: Use different email address

---

---

# ✅ VERIFYING EVERYTHING WORKS

## Full Test Checklist

- [ ] MySQL installed and running
- [ ] Python and required libraries installed
- [ ] Project folder created with 3 files
- [ ] Backend code in app.py
- [ ] Frontend code in index.html
- [ ] requirements.txt filled
- [ ] Flask app starts without errors
- [ ] Website loads at http://localhost:5000
- [ ] Home page displays correctly
- [ ] Can register with valid data
- [ ] Success popup appears
- [ ] Can view registrations
- [ ] Data persists (reload page, data still there)
- [ ] Can't register with duplicate email
- [ ] All navigation buttons work

---

---

# 🎓 PROJECT WALKTHROUGH

## Understanding the Full Flow

### 1. User Opens Website

Browser makes HTTP GET request to `http://localhost:5000/`

↓

Flask `@app.route("/")` catches it

↓

Serves `index.html` file

↓

Browser loads HTML, CSS, JavaScript

### 2. User Fills Form & Submits

JavaScript event listener catches form submission

↓

Validates form (category, workshop, all fields filled)

↓

JavaScript sends POST request to `/api/register` with form data

↓

### 3. Backend Processes Request

Flask `@app.route("/api/register", methods=["POST"])` catches it

↓

Extracts form data using `request.form.get()`

↓

Validates all fields not empty

↓

Creates MySQL connection using `get_db()`

↓

Executes INSERT SQL query with student data

↓

If email already exists: Returns 409 error

↓

If success: Returns 201 status code

↓

### 4. Frontend Handles Response

JavaScript receives response

↓

If 201: Show success popup, reset form, hide workshops

↓

If error: Show red alert message

↓

### 5. User Views Registrations

User clicks "View Registrations"

↓

JavaScript calls `loadRegistrations()`

↓

Makes GET request to `/api/registrations`

↓

Backend fetches all rows from MySQL using SELECT query

↓

Formats as HTML table with styling

↓

Returns HTML table

↓

JavaScript displays table in page

↓

User sees all registrations!

