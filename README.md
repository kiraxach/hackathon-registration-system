# hackathon-registration-system
Hackathon 2026 Full Stack Registration Form

# 🌩️ Hackathon 2026 Registration System

*(Full Stack Capstone Project — Detailed Implementation Guide)*

---

# 📌 1. Introduction

This project is a **full-stack web application** developed as part of my capstone project.

The purpose of this system is to:

* Allow students to register for a hackathon
* Let them choose workshop categories and time slots
* Store all user data in a database
* Display all registrations in a structured format

This project demonstrates:

* Frontend development
* Backend API handling
* Database connectivity
* Real-world application workflow

---

# 🧰 2. Technologies Used (Explained)

## 🎨 Frontend

### HTML

Used to create the structure of the website:

* Forms
* Buttons
* Pages (Home, Register, View)

### CSS

Used for styling:

* Dark theme UI
* Neon glow effects
* Animations (hover, transitions)
* Layout using flexbox and grid

### JavaScript

Used for:

* Handling form submission
* Making API calls (`fetch()`)
* Switching between pages
* Validating user input

---

## ⚙️ Backend

### Python + Flask

Flask is used to:

* Create server
* Handle routes (URLs)
* Process form data
* Connect to database

---

## 🗄️ Database

### MySQL

Used to:

* Store user data permanently
* Ensure email uniqueness
* Retrieve and display data

---

# 🧱 3. Project Structure

```id="struct1"
project-folder/
│
├── app.py              # Backend logic (Flask server)
├── index.html          # Frontend UI
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

# ⚙️ 4. COMPLETE SETUP (VERY DETAILED)

---

## 🖥️ Step 1: Install VS Code

1. Go to https://code.visualstudio.com/
2. Click Download
3. Install normally (Next → Next → Finish)
4. Open VS Code

---

## 🔌 Step 2: Install Python Extension

1. Open Extensions panel
2. Search → `Python`
3. Click Install

This helps VS Code understand Python code.

---

## 🐍 Step 3: Install Python

1. Go to https://www.python.org/downloads/
2. Download latest version
3. IMPORTANT:

   * ✔ Tick **Add Python to PATH**

Check installation:

```bash id="pycheck"
python --version
```

---

## 📦 Step 4: Install Required Libraries (VERY IMPORTANT)

Open terminal in VS Code:

```bash id="pip1"
pip install flask
```

```bash id="pip2"
pip install mysql-connector-python
```

These libraries are used for:

* Flask → backend server
* mysql-connector → database connection

---

## 🛢️ Step 5: Install MySQL

Follow:
https://nkgacademy.com/how-to-download-mysql-and-install-command-line-client-on-windows/

### While installing:

* Username → `root`
* Password → `root`

⚠️ This must match backend code.

---

## ▶️ Step 6: Check MySQL is Running

```bash id="mysqlcheck"
mysql -u root -p
```

Enter:

```id="mysqlpass"
root
```

If it opens → success ✅

---

## 📄 Step 7: Create Files

Inside project folder create:

* `app.py`
* `index.html`
* `requirements.txt`

---

## 📦 Step 8: requirements.txt

```id="reqfile"
flask
mysql-connector-python
```

---

# 🧠 5. BACKEND CODE (LINE-BY-LINE EXPLANATION)

```python
from flask import Flask, request, send_from_directory
```

➡ Imports Flask and request handling tools

```python
import mysql.connector
```

➡ Used to connect Python with MySQL

```python
import os
```

➡ Used to handle file paths

---

```python
app = Flask(__name__)
```

➡ Creates Flask application

---

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "hackathon_db"
}
```

➡ Stores database credentials

---

```python
def get_db():
    return mysql.connector.connect(**DB_CONFIG)
```

➡ Function to create database connection

---

```python
def init_db():
```

➡ This function initializes database

```python
cur.execute("CREATE DATABASE IF NOT EXISTS hackathon_db")
```

➡ Creates database if not exists

```python
CREATE TABLE registrations
```

➡ Creates table for storing data

---

```python
@app.route("/")
```

➡ Home route

```python
return send_from_directory(..., "index.html")
```

➡ Serves frontend file

---

```python
@app.route("/api/register", methods=["POST"])
```

➡ API to register users

```python
request.form.get()
```

➡ Gets data from form

---

```python
INSERT INTO registrations
```

➡ Stores data in database

---

```python
@app.route("/api/registrations")
```

➡ API to fetch all users

---

```python
if __name__ == "__main__":
```

➡ Entry point of program

```python
init_db()
```

➡ Creates DB automatically

```python
app.run(debug=True)
```

➡ Starts server

---

# 🎨 6. FRONTEND EXPLANATION (VERY DETAILED)

## HTML

* Forms for input
* Buttons for navigation
* Sections for pages

## CSS

* Dark background
* Neon blue theme
* Animations (hover, glow)

## JavaScript

### Form Submission:

```javascript
fetch('/api/register')
```

➡ Sends data to backend

### Page Navigation:

```javascript
showPage()
```

➡ Switches between pages
------------------------------------------- FRONT END CODE -----------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hackathon 2026 - Registration</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Courier New', monospace; background: linear-gradient(135deg, #0f1419 0%, #1a1f2e 100%); color: #0ff; min-height: 100vh; padding: 20px; }
.wrapper { max-width: 900px; margin: 0 auto; }
.nav-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 40px; padding-bottom: 20px; border-bottom: 2px solid #0ff; animation: slideDown 0.8s ease-out; }
@keyframes slideDown { from { transform: translateY(-50px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
.logo { font-size: 24px; font-weight: bold; text-shadow: 0 0 20px #0ff; letter-spacing: 3px; }
.nav-buttons { display: flex; gap: 15px; }
.nav-btn { background: transparent; border: 2px solid #0ff; color: #0ff; padding: 8px 20px; cursor: pointer; font-family: inherit; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; border-radius: 3px; transition: all 0.3s ease; }
.nav-btn:hover, .nav-btn.active { background: #0ff; color: #0f1419; box-shadow: 0 0 15px #0ff; transform: translateY(-2px); }
.page { display: none; animation: fadeIn 0.8s ease-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.page.active { display: block; }
.page-title { font-size: 32px; margin-bottom: 30px; text-shadow: 0 0 20px #0ff; letter-spacing: 2px; animation: glow 3s ease-in-out infinite; }
@keyframes glow { 0%,100% { text-shadow: 0 0 10px #0ff; } 50% { text-shadow: 0 0 30px #0ff,0 0 40px #00ffff; } }
.event-card { background: rgba(26, 31, 46, 0.9); border: 2px solid #0ff; border-radius: 5px; padding: 25px; margin-bottom: 20px; animation: slideUp 0.7s ease-out; }
@keyframes slideUp { from { transform: translateY(30px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
.event-card h2 { color: #0ff; font-size: 20px; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 1px; }
.event-card p { color: #0af; font-size: 14px; line-height: 1.6; margin-bottom: 15px; }
.info-row { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 15px 0; font-size: 13px; }
.info-item { background: rgba(15, 20, 25, 0.8); padding: 12px; border-left: 3px solid #0ff; border-radius: 2px; }
.info-label { color: #0ff; font-weight: bold; text-transform: uppercase; font-size: 11px; margin-bottom: 5px; }
.info-value { color: #0af; font-size: 14px; }
.cta-button { background: #0ff; color: #0f1419; border: none; padding: 12px 30px; font-size: 14px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; cursor: pointer; border-radius: 3px; margin-top: 15px; transition: all 0.3s ease; font-family: inherit; }
.cta-button:hover { transform: translateY(-3px); box-shadow: 0 0 20px #0ff; }
.form-section { animation: slideUp 0.7s ease-out; }
.form-group { margin-bottom: 20px; animation: slideUp 0.7s ease-out; }
label { display: block; color: #0ff; font-size: 13px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; font-weight: bold; }
input, select, textarea { width: 100%; padding: 12px; background: rgba(15, 20, 25, 0.9); border: 2px solid #0ff; color: #0ff; font-family: inherit; font-size: 14px; border-radius: 3px; transition: all 0.3s ease; }
input:focus, select:focus, textarea:focus { outline: none; box-shadow: 0 0 15px #0ff; background: rgba(0, 255, 255, 0.05); border-color: #00ffff; }
select option { background: #0f1419; color: #0ff; }

/* Workshop radio cards */
.workshop-cards { display: flex; flex-direction: column; gap: 10px; margin-top: 8px; }
.workshop-card { display: flex; align-items: center; gap: 12px; padding: 14px 16px; background: rgba(15, 20, 25, 0.8); border-radius: 3px; border: 1px solid #0ff; transition: all 0.3s ease; cursor: pointer; }
.workshop-card:hover { background: rgba(0, 255, 255, 0.08); box-shadow: 0 0 10px #0ff; }
.workshop-card input[type="radio"] { width: auto; margin: 0; cursor: pointer; accent-color: #0ff; }
.workshop-card label { margin: 0; cursor: pointer; flex: 1; font-size: 14px; text-transform: none; letter-spacing: 0; font-weight: normal; }
.workshop-card .workshop-badge { font-size: 10px; background: rgba(0,255,255,0.1); border: 1px solid #0ff; color: #0ff; padding: 2px 8px; border-radius: 2px; text-transform: uppercase; letter-spacing: 1px; white-space: nowrap; }
.workshops-hidden { display: none; }

/* Category hint */
.category-hint { font-size: 12px; color: #0af; margin-top: 8px; padding: 8px 12px; background: rgba(0,255,255,0.05); border-left: 2px solid #0af; border-radius: 2px; display: none; }
.category-hint.show { display: block; }

.submit-btn { background: #0ff; color: #0f1419; border: none; padding: 14px 40px; font-size: 15px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; cursor: pointer; border-radius: 3px; width: 100%; margin-top: 20px; transition: all 0.3s ease; font-family: inherit; }
.submit-btn:hover { transform: translateY(-2px); box-shadow: 0 0 25px #0ff; }
.popup { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.8); justify-content: center; align-items: center; z-index: 1000; animation: fadeIn 0.3s ease-out; }
.popup.show { display: flex; }
.popup-content { background: #0f1419; border: 3px solid #0ff; padding: 30px; border-radius: 5px; text-align: center; max-width: 400px; box-shadow: 0 0 30px #0ff; animation: popupScale 0.4s ease-out; }
@keyframes popupScale { from { transform: scale(0.8); opacity:0;} to {transform: scale(1); opacity:1;} }
.popup-content h2 { color: #0ff; font-size: 24px; margin-bottom: 15px; text-shadow: 0 0 20px #0ff; letter-spacing: 2px; }
.popup-content p { color: #0af; font-size: 14px; line-height: 1.6; margin-bottom: 20px; }
.popup-btn { background: #0ff; color: #0f1419; border: none; padding: 10px 25px; font-size: 13px; font-weight: bold; cursor: pointer; border-radius: 3px; transition: all 0.3s ease; font-family: inherit; text-transform: uppercase; letter-spacing: 1px; }
.popup-btn:hover { transform: translateY(-2px); box-shadow: 0 0 15px #0ff; }
.day-schedule { background: rgba(15,20,25,0.8); border:2px solid #0ff; padding:15px; border-radius:3px; margin-bottom:15px; }
.day-schedule h3 { color:#0ff; font-size:16px; margin-bottom:10px; text-transform:uppercase; }
.schedule-item { color:#0af; font-size:13px; padding:8px 0; border-bottom:1px solid rgba(0,255,255,0.2); }
.schedule-item:last-child { border-bottom:none; }
.time { color:#0ff; font-weight:bold; }
.alert { padding:15px; margin-bottom:20px; border-radius:3px; border-left:4px solid; display:none; }
.alert.success { background: rgba(0,255,100,0.1); border-color:#0f0; color:#0f0; display:block; }
.alert.error { background: rgba(255,0,100,0.1); border-color:#f00; color:#f00; display:block; }
</style>
</head>
<body>
<div class="wrapper">
<div class="nav-bar">
<div class="logo">&gt; EVENT.HUB</div>
<div class="nav-buttons">
<button class="nav-btn active" onclick="showPage('home')">Home</button>
<button class="nav-btn" onclick="showPage('register')">Register</button>
<button class="nav-btn" onclick="showPage('view')">View Registrations</button>
</div>
</div>

<!-- HOME PAGE -->
<div id="home" class="page active">
<div class="page-title">HACKATHON 2026</div>
<div class="event-card">
<h2>Welcome to the Ultimate Coding Challenge</h2>
<p>Join hundreds of students for an intense 2-day hackathon experience. Build, compete, and showcase your skills!</p>
</div>
<div class="event-card">
<h2>Event Details</h2>
<div class="info-row">
<div class="info-item"><div class="info-label">Dates</div><div class="info-value">March 22-23, 2026</div></div>
<div class="info-item"><div class="info-label">Location</div><div class="info-value">Tech Campus - Hall A</div></div>
<div class="info-item"><div class="info-label">Duration</div><div class="info-value">48 Hours Non-Stop</div></div>
<div class="info-item"><div class="info-label">Level</div><div class="info-value">Beginner Friendly</div></div>
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

<!-- REGISTER PAGE -->
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

  <!-- STEP 2: Choose 1 workshop from the selected category (2 options shown) -->
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

<!-- VIEW REGISTRATIONS -->
<div id="view" class="page">
<div class="page-title">VIEW REGISTRATIONS</div>
<div class="event-card">
<h2>All Registered Students</h2>
<div id="registrationsList"></div>
</div>
</div>
</div>

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
function showPage(pageName){
  const pages=document.querySelectorAll('.page');
  const navBtns=document.querySelectorAll('.nav-btn');
  pages.forEach(p=>p.classList.remove('active'));
  navBtns.forEach(b=>b.classList.remove('active'));
  document.getElementById(pageName).classList.add('active');
  event.target.classList.add('active');
  if(pageName==='view') loadRegistrations();
  window.scrollTo(0,0);
}

function showWorkshops(category){
  // Hide all workshop groups first
  ['cyber','datascience','aiml'].forEach(c=>{
    document.getElementById('workshops-'+c).style.display='none';
  });
  // Clear any previously selected radio
  document.querySelectorAll('input[name="workshop"]').forEach(r=>r.checked=false);

  const section = document.getElementById('workshopSection');
  const hint    = document.getElementById('categoryHint');

  if(!category){
    section.style.display='none';
    hint.classList.remove('show');
    return;
  }

  // Show the right group
  document.getElementById('workshops-'+category).style.display='flex';
  section.style.display='block';
  hint.classList.add('show');

  const labels = {
    cyber:       'Cybersecurity — choose 1 of 2 workshops below.',
    datascience: 'Data Science — choose 1 of 2 workshops below.',
    aiml:        'AI / Machine Learning — choose 1 of 2 workshops below.'
  };
  hint.textContent = labels[category];
}

function showAlert(message,type){
  const alertDiv=document.getElementById('alertMessage');
  alertDiv.textContent=message;
  alertDiv.className=`alert ${type}`;
  setTimeout(()=>{alertDiv.className='alert';},5000);
}

function closePopup(){ document.getElementById('successPopup').classList.remove('show'); showPage('home'); }

document.getElementById('registrationForm').addEventListener('submit', async function(e){
  e.preventDefault();

  const category = document.getElementById('workshopCategory').value;
  if(!category){ showAlert('Please select a workshop category.','error'); return; }

  const selectedWorkshop = document.querySelector('input[name="workshop"]:checked');
  if(!selectedWorkshop){ showAlert('Please select a workshop from the category.','error'); return; }

  const params = new URLSearchParams({
    fullName:   document.getElementById('fullName').value,
    email:      document.getElementById('email').value,
    university: document.getElementById('university').value,
    workshops:  selectedWorkshop.value,   // single workshop chosen
    category:   category,
    timeslot:   document.getElementById('timeslot').value
  });

  try{
    const res  = await fetch('/api/register',{ method:'POST', body: params });
    const text = await res.text();
    if(res.status===201){
      document.getElementById('registrationForm').reset();
      showWorkshops('');
      document.getElementById('workshopCategory').value='';
      document.getElementById('successPopup').classList.add('show');
    } else {
      showAlert(text,'error');
    }
  } catch(err){ showAlert('Server error. Please try again.','error'); }
});

async function loadRegistrations(){
  const div=document.getElementById('registrationsList');
  try{
    const res=await fetch('/api/registrations');
    div.innerHTML=await res.text();
  } catch(err){ div.innerHTML="<p style='color:#f00'>Cannot load registrations.</p>"; }
}
</script>
</body>
</html>


----------------------------------------- BACKEND CODE ------------------------------------------------
from flask import Flask, request, send_from_directory
import mysql.connector
import os

app = Flask(__name__)

# ─────────────────────────────────────────
#  MySQL Configuration — update as needed
# ─────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",          # your MySQL username
    "password": "root",           # your MySQL password
    "database": "hackathon_db"
}


def get_db():
    """Return a fresh MySQL connection."""
    return mysql.connector.connect(**DB_CONFIG)


def init_db():
    """Create the database and table if they don't exist."""
    # Connect without selecting a database first
    conn = mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    cur.execute(f"USE {DB_CONFIG['database']}")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id         INT AUTO_INCREMENT PRIMARY KEY,
            full_name  VARCHAR(255)  NOT NULL,
            email      VARCHAR(255)  NOT NULL UNIQUE,
            university VARCHAR(255)  NOT NULL,
            workshops  VARCHAR(255)  NOT NULL,   -- comma-separated pair
            timeslot   VARCHAR(100)  NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("✅  Database & table ready.")


# ─────────────────────────────────────────
#  Serve the front-end
# ─────────────────────────────────────────
@app.route("/")
def index():
    """Serve the HTML file sitting next to app.py."""
    return send_from_directory(os.path.dirname(__file__), "index.html")


# ─────────────────────────────────────────
#  POST /api/register
# ─────────────────────────────────────────
@app.route("/api/register", methods=["POST"])
def register():
    full_name  = request.form.get("fullName",    "").strip()
    email      = request.form.get("email",       "").strip()
    university = request.form.get("university",  "").strip()
    timeslot   = request.form.get("timeslot",    "").strip()
    workshops = request.form.get("workshops", "").strip()  # list from checkboxes

    # ── Validation ──────────────────────────────────────────────────────
    if not all([full_name, email, university, timeslot]):
        return "All fields are required.", 400
    
    workshops_str = workshops

    # ── Insert into MySQL ────────────────────────────────────────────────
    try:
        conn = get_db()
        cur  = conn.cursor()
        cur.execute("""
            INSERT INTO registrations (full_name, email, university, workshops, timeslot)
            VALUES (%s, %s, %s, %s, %s)
        """, (full_name, email, university, workshops_str, timeslot))
        conn.commit()
        cur.close()
        conn.close()
        return "Registration successful.", 201

    except mysql.connector.errors.IntegrityError:
        return "This email is already registered.", 409

    except Exception as e:
        print(f"DB error: {e}")
        return "Server error. Please try again.", 500


# ─────────────────────────────────────────
#  GET /api/registrations  (HTML table)
# ─────────────────────────────────────────
@app.route("/api/registrations", methods=["GET"])
def view_registrations():
    try:
        conn = get_db()
        cur  = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM registrations ORDER BY created_at DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"DB error: {e}")
        return "<p style='color:#f00'>Could not load registrations.</p>", 500

    if not rows:
        return "<p style='color:#0af;text-align:center;padding:20px'>No registrations yet.</p>"

    # Build an HTML table that matches the existing dark/cyan theme
    html = """
    <style>
        .reg-table { width:100%; border-collapse:collapse; font-size:13px; }
        .reg-table th {
            background:rgba(0,255,255,0.15); color:#0ff;
            padding:10px 14px; text-align:left;
            text-transform:uppercase; letter-spacing:1px;
            border-bottom:2px solid #0ff;
        }
        .reg-table td {
            color:#0af; padding:10px 14px;
            border-bottom:1px solid rgba(0,255,255,0.15);
        }
        .reg-table tr:hover td { background:rgba(0,255,255,0.05); }
        .badge {
            display:inline-block; padding:3px 8px;
            background:rgba(0,255,255,0.1); border:1px solid #0ff;
            border-radius:3px; font-size:11px; margin:2px 2px 2px 0;
        }
    </style>
    <table class="reg-table">
      <thead>
        <tr>
          <th>#</th><th>Name</th><th>Email</th>
          <th>University</th><th>Workshops</th>
          <th>Time Slot</th><th>Registered At</th>
        </tr>
      </thead>
      <tbody>
    """

    for i, r in enumerate(rows, 1):
        workshop_badges = "".join(
            f'<span class="badge">{w.strip()}</span>'
            for w in r["workshops"].split(",")
        )
        html += f"""
        <tr>
          <td>{i}</td>
          <td>{r['full_name']}</td>
          <td>{r['email']}</td>
          <td>{r['university']}</td>
          <td>{workshop_badges}</td>
          <td>{r['timeslot']}</td>
          <td>{r['created_at'].strftime('%b %d, %Y  %H:%M')}</td>
        </tr>"""

    html += "</tbody></table>"
    return html


# ─────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────
if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)
--------------------------------------------------------------------------------------------------------------------------------------------------


### Data Loading:

```javascript
loadRegistrations()
```

➡ Fetches data from backend

---

# 🔁 7. WORKING FLOW (STEP-BY-STEP)

1. User opens website
2. Clicks Register
3. Fills form
4. Clicks Submit
5. JavaScript sends data
6. Flask receives request
7. Data stored in MySQL
8. User views registrations

---

# 🧪 8. TESTING

* Fill form
* Submit
* Check success message
* Open View page
* Verify data

---

# ⚠️ 9. COMMON ERRORS

## MySQL Error

✔ Start MySQL server
✔ Check credentials

## Module Error

```bash
pip install flask mysql-connector-python
```

---

# 📸 10. SCREENSHOTS



# 🚀 11. FUTURE IMPROVEMENTS

* Login system
* Admin panel
* Cloud deployment
* Email notifications



# 👩‍💻 12. AUTHOR

Keerthana Chebolu

# 🎉 FINAL NOTE

This project demonstrates:

* Full stack development
* Database integration
* Real-world application building


