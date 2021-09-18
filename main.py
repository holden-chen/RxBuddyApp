# Holden Chen
# 09/18/2021
# RxBuddyApp - A Flask app that shows the user the common side effects for a given medication.

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    medication = request.args.get("medication", "")
    if medication:
        med_side_effects = side_effects(medication)
    else:
        med_side_effects = ""
    return """<form action="" method="get">
                <input type="text" name="medication">
                <input type="submit" value="Show Side Effects">
            </form>""" + med_side_effects
    

def side_effects(medication):
    """Returns the common side effects for a given medication."""
    try:
        med_dict = {
            "Atorvastatin": "headaches, nausea, diarrhea",
            "Gabapentin": "dizziness, drowsiness",
            "Metformin": "nausea, vomiting, diarrhea"
            }
        if medication in med_dict:
            return med_dict[medication]
        else:
            return "NOT FOUND"
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)
