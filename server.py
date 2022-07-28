from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, Quote
import os
import crud
from jinja2 import StrictUndefined
#from dateutil.parser import parse
from random import choice, randint


app = Flask(__name__)
app.sekret_key="dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/about")
def main_page():
    return render_template("about.html")

@app.route("/")
def homepage():
    authors = crud.get_all_authors()
    return render_template("homepage.html", authors=authors)

@app.route("/passage")
def passage():
    return passage

@app.route("/random")
def random_quote():
    quote = crud.get_random_quote()
    return render_template("passage.html", quote=quote)
    
@app.route("/search")
def search():
    author = request.args.get('author')
    quote = crud.get_quote_by_author(author)
    return render_template("passage.html", quote=quote)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)