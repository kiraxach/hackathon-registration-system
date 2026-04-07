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
