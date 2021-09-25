# Holden Chen
# 09/18/2021
# RxBuddyApp - A Flask app that shows the user the common side effects for a given medication.

from sqlite3.dbapi2 import connect
from flask import Flask, render_template, request, g
from datetime import datetime
import sqlite3

from flask.templating import render_template_string


app = Flask(__name__)


def connect_db():
    medications_db = sqlite3.connect('medications.db', check_same_thread=False)
    medications_db.row_factory = sqlite3.Row
    return medications_db

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite3_db.close()


def get_side_effects(medication):
    """Returns the common side effects for a given medication."""
    try:
        user_med = medication.lower()
        db = get_db()

        query = """SELECT * FROM medications WHERE drug_name = ?"""
        arg = (user_med,)
        cursor = db.execute(query, arg)
        results = cursor.fetchone()
        cursor.close()

        return results[2]
    except ValueError:
        return "ERROR"

# Index page with the UI
@app.route("/", methods=["POST", "GET"])
def index():
    medication = request.form.get("medication", "")
    if medication:
        results = get_side_effects(medication)
    else:
        results = "NOT FOUND"
    return render_template("index.html", results=results, med_name=medication)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)
