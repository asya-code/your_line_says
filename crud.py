from model import db, Quote, connect_to_db
from random import choice

def create_quote(text, author):
    """Create and return a new quote."""
    quote = Quote(text=text, author=author)
    return quote


def get_quote_by_author(given_author):
    """Return random quote by particular author."""
    return choice(Quote.query.filter(Quote.author==given_author).all())

def get_random_quote():
    """Return random quote by any author."""
    return choice(Quote.query.all())


if __name__ == "__main__":
    from server import app
    connect_to_db(app)