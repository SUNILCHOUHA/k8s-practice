from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "/data/notes.db"

def init_db():
    os.makedirs("/data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS notes (text TEXT)")
    conn.close()

@app.route("/api/notes", methods=["POST"])
def add_note():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO notes VALUES (?)", (data["note"],))
    conn.commit()
    conn.close()
    return {"status": "saved"}

@app.route("/api/notes")
def get_notes():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT text FROM notes").fetchall()
    conn.close()
    return jsonify([r[0] for r in rows])

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)