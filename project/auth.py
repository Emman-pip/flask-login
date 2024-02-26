from flask import blueprint, render_template, url_for, redirect, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from . import db


auth = blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login")


@auth.route("/signup")
def signup(): 
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup(): 
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    
    if user:
        flash('You already have an account.')
        return redirect(url_for('auth.login'))
        
    
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))

@auth.route("/logout")
def logout():
    return "logout"
