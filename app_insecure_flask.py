from flask import Flask, request, make_response
import sqlite3, os

app = Flask(__name__)

# ❌ Hardcoded secret key (fake placeholder). Do NOT do this.
app.secret_key = "FAKE-SECRET-KEY-DO-NOT-USE-1234567890"

DB_PATH = "example.db"

def init_db():
    # ❌ No proper migrations or schema management.
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    # Seed demo user (password is "password")
    cur.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'password')")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    # ❌ Reflected XSS via unsanitized parameter
    name = request.args.get("name", "world")
    return f"<h1>Hello, {name}!</h1>"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # ❌ SQL Injection vulnerable (string interpolation into SQL)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'"
    print("DEBUG SQL (insecure):", query)
    try:
        cur.execute(query)  # ⚠️ vulnerable
        row = cur.fetchone()
    finally:
        conn.close()

    if row:
        resp = make_response("Logged in (insecure)")
        # ❌ Sets a cookie without secure flags
        resp.set_cookie("session", "fake-session-token", httponly=False, secure=False)
        return resp
    return "Invalid credentials", 401

@app.route("/unsafe_echo")
def unsafe_echo():
    # ❌ Command injection via os.system
    msg = request.args.get("msg", "hi")
    os.system("echo " + msg)  # ⚠️ vulnerable
    return "Echoed (maybe)."

if __name__ == "__main__":
    init_db()
    # ❌ Debug mode exposes internals in production
    app.run(host="0.0.0.0", port=5000, debug=True)