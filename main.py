# Holden Chen
# Updated 01/04/2022
# RxBuddyApp - A Flask app that shows the user the common side effects for a given medication.

from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import json
import os


app = Flask(__name__)

load_dotenv()  # take environmental variable from .env.

API_KEY = os.getenv("API_KEY")

# Index page with the UI
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        drug_1 = request.form["drug_1"]
        drug_2 = request.form["drug_2"]
        drug_3 = request.form["drug_3"]
        drug_4 = request.form["drug_4"]
        drug_dict = {drug_1: None, drug_2: None, drug_3: None, drug_4: None}

        for drug_name in drug_dict:
            if drug_name == "":
                continue
            url = f"https://api.fda.gov/drug/label.json?api_key={API_KEY}&search=adverse_reactions:{drug_name}"
            req = requests.get(url)
            drug_data = json.loads(req.content)
            drug_dict[drug_name] = drug_data["results"][0]["adverse_reactions"][0]

        return render_template("index.html", drug_dict=drug_dict)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)
