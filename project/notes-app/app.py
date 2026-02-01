import os
from flask import Flask

app = Flask(__name__)

DATA_DIR = os.environ.get("DATA_DIR", "/data")
FILE_PATH = f"{DATA_DIR}/notes.txt"

@app.route("/")
def home():
    return "Notes App with ConfigMap + Ingress"

@app.route("/write")
def write():
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(FILE_PATH, "a") as f:
        f.write("Hello from Kubernetes with ConfigMap\n")
    return "Written"

@app.route("/read")
def read():
    try:
        with open(FILE_PATH) as f:
            return f.read()
    except:
        return "No data"

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=5000)
