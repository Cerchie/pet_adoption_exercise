from flask import Flask, render_template, flash, redirect, flash, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet


from forms import AddPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def list_pets():
    """Show homepage links."""
    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)

@app.route("/add")
def add_pet():
    """show page for adding a pet"""
    return render_template("adding_a_pet.html")
