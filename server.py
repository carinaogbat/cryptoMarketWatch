from flask import Flask
from model import connect_to_db, User, Crypto, Watchlist
import os
import crud

app = Flask(__name__)
app.secret_key = "dev"

#Members API route
@app.route("/members")
def members():

    return {"members": ["member1", "member1", "member3"]}
  

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)
