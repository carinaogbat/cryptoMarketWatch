"""Models for Crypto Market Watch"""

from flask_sqlalchemy import SQLAlchemy

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


class Crypto(db.model):
    """A cryptocurrency"""

    __tablename__ = "cryptos"

    crypto_id = db.column(db.Integer, autoincrement=True, primary_key=True)
    crypto_name = db.column(db.String)
    crypto_price = db.column(db.Decimal)
    crypto_market_history = db.column(db.String)
    crypto_about = db.column(db.String)

    watchlists = db.relationship("Watchlist", back_populates="cryptos")
    user = db.relationship("User", back_populates="cryptos")

    def __repr__(self):
        return f"<Crypto crypto_id: {self.crypto_id}, crypto_name: {self.crypto_name}"

    
class Watchlist(db.model):
    """Watchlist"""

    __tablename__ = "watchlists"

    watchlist_id = db.column(db.Integer, autoincrement=True, primary_key=True)
    crypto_id = db.column(db.Integer, db.ForeignKey("cryptos.crypto_id"))
    user_id = db.column(db.Integer, db.ForeignKey("users.user_id"))

    cryptos = db.relationship("Crypto", back_populates="watchlists")
    user = db.relationship("User", back_populates="watchlists")

    def __repr__(self):
        return f"Watchlist watchlist_id: {self.watchlist_id}, crypto_id = {self.crypto_id}"
