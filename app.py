from flask import Flask, render_template, flash, redirect, flash, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet


from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

DEBUG_TB_INTERCEPT_REDIRECTS = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def list_pets():
    """Show homepage links."""
    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        # new_pet = Pet(name=form.name.data, age=form.age.data, ...)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect(url_for('list_pets'))

    else:
        # re-present form for editing
        return render_template("adding_a_pet.html", form=form)

    """show page for adding a pet"""
    return render_template("adding_a_pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('list_pets'))

    else:
        # failed; re-present form for editing
        return render_template("pet_edit_form.html", form=form, pet=pet)
