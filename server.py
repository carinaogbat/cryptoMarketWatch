from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
from model import connect_to_db, User, Crypto, Watchlist
import os
import crud

app = Flask(__name__)
app.secret_key = "dev"

@app.route('/')
def homepage():
    """Returns homepage"""

    return render_template('index.html')


    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
