"""Script to seed database."""

import os
import csv
import crud, model, server

os.system("dropdb stichom")
os.system("createdb stichom")

model.connect_to_db(server.app)
model.db.create_all()

# Create quotes from file
#quotes_file = open("quotes_all.csv")
#quotes = list(csv.reader(quotes_file, delimiter=';'))
with open("quotes_all.csv") as csv_file:
    quote_reader = csv.reader(csv_file, delimiter=";")
    for line in quote_reader:
        ready_quote = crud.create_quote(text=line[0], author=line[1])
        model.db.session.add(ready_quote)
model.db.session.commit()


# ready_quotes = []
# for quote in quotes:
#     #print(quote)
#     ready_quote = crud.create_quote(text=quote[0], author=quote[1])
#     ready_quotes.append(ready_quote)
#     model.db.session.add(quote)
# model.db.session.commit()
