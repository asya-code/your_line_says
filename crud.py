from model import db, Quote, connect_to_db
from random import choice

def create_quote(text, author):
    """Create and return a new quote."""
    quote = Quote(text=text, author=author)
    return quote


def get_quote_by_author(given_author):
    """Return random quote by particular author."""
    all_quotes = Quote.query.filter(Quote.author.contains(given_author)).all()
    if len(all_quotes) > 0:
        return choice(all_quotes)
    else:
        return create_quote(text="unfortinately, we don't have that author yet", author="Your line")
    #return choice(Quote.query.filter(Quote.author==given_author).all())

def get_random_quote():
    """Return random quote by any author."""
    all_quotes = Quote.query.all()
    return choice(all_quotes)

def get_all_authors():
    """Returns list of all authors"""
    all_authors = []
    all_quotes = Quote.query.all()
    for quote in all_quotes:
        all_authors.append(quote.author)

    '''
    for author in all_quotes.keys():
        all_authors.append(author)
    '''
    return all_authors


if __name__ == "__main__":
    from server import app
    connect_to_db(app)