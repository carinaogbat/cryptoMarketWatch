"""Models for Crypto Market Watch"""

from flask_sqlalchemy import SQLAlchemy

# test_user = User(email='test', password='test')

db = SQLAlchemy()

class User(db.Model):
    """A User"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    watchlists = db.relationship("Watchlist", back_populates="user")
    cryptos = db.relationship("Crypto", back_populates="user")

    def __repr__(self):
        return f"<User user_id = {self.user_id} email = {self.email}"


class Crypto(db.Model):
    """A cryptocurrency"""

    __tablename__ = "cryptos"

    crypto_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    crypto_name = db.Column(db.String)
    crypto_price = db.Column(db.DECIMAL)
    crypto_market_history = db.Column(db.String)
    crypto_about = db.Column(db.String)
    user_id = db.Column(db.ForeignKey("users.user_id"))

    watchlists = db.relationship("Watchlist", back_populates="cryptos")
    user = db.relationship("User", back_populates="cryptos")

    def __repr__(self):
        return f"<Crypto crypto_id: {self.crypto_id}, crypto_name: {self.crypto_name}"

    
class Watchlist(db.Model):
    """Watchlist"""

    __tablename__ = "watchlists"

    watchlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    crypto_id = db.Column(db.Integer, db.ForeignKey("cryptos.crypto_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    cryptos = db.relationship("Crypto", back_populates="watchlists")
    user = db.relationship("User", back_populates="watchlists")

    def __repr__(self):
        return f"Watchlist watchlist_id: {self.watchlist_id}, crypto_id = {self.crypto_id}"

    
def connect_to_db(flask_app, db_uri="postgresql:///crypto", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
