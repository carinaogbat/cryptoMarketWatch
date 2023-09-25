"""Models for Crypto Market Watch"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A User"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id = {self.user_id} email = {self.email}"