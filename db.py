from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# We have got a object which is SQLAlchemy and that is essentiallyi
# a thing that is going to link to our flask app and it is going to
# look at all of the objects that we tell it to. And then its going
# to allow us to map those objects to rows in a database.

# When we create an item model object that has a column called name
# and a column called price, its going to allow us to very easily
# put that object into our database.
#
# Naturally putting an object into a database, all that is saving is
# the object's properties into the database.
