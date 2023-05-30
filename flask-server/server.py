
from flask import Flask
import main as run_app
import os
import json
import sys


app = Flask(__name__)

#  Members API route

@app.route("/members")
def members():
    os.system("python main.py 'chat'")
    f = open('data.json')
    data = json.load(f)
    return data

if __name__ == "__main__":
    app.run(debug=True)