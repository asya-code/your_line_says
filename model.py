from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Quote(db.Model):
    """A quote."""
    __tablename__ = "quotes"

    quote_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text = db.Column(db.String(),  nullable=False)
    author = db.Column(db.String(75), nullable=False)
   
    def __repr__(self):
        return f"<Quote quote_id={self.quote_id}, author={self.author}>"


def connect_to_db(app, db_uri="postgresql:///stichom", echo=True):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)
