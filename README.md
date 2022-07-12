# RaBraceletsStore
Here is my Bracelets Store which is called Ra

# Technology
Python, Flask, MVC model, HTML, CSS, Bootstrap 4

# Available Scripts
In the project directory, you can run: run.py (python)

# What we don't do
Login page Add product to shopping cart

# How to insert data
Step 1: In file __init__.py
Remove comment on line 26, 27
Step 2:
Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

    from store import db, create_app
    db.create_all(app=create_app())
    quit()
