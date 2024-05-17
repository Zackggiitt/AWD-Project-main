from flask import Blueprint, render_template, request, url_for, redirect, session, jsonify
import json
from werkzeug.security import check_password_hash
from werkzeug.security import check_password_hash, generate_password_hash
from apps.models import AccountDimension, RecipeDimension
from apps import db
from apps.form import LoginForm
from flask import flash
BP = Blueprint('auth', __name__, url_prefix='/auth')


@BP.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = AccountDimension.query.filter_by(username=username).first()
            if not user or not check_password_hash(user.password, password):
                flash('Invalid username or password', 'error')
                return redirect(url_for('auth.login'))
            else:
                session["username"] = username
                session["user_id"] = user.user_id
                flash('You were successfully logged in', 'success')
                return redirect(url_for('auth.main'))
        else:
            flash('Login failed. Please check your credentials and try again.', 'error')
            return redirect(url_for('auth.login'))


@BP.route("/account", methods=['GET', 'POST'])
def account():
    return render_template("account.html")


@BP.route("/Main", methods=['GET', 'POST'])
def main():
    recipes = RecipeDimension.query.all()
    return render_template("Main.html",recipes=recipes)


@BP.route("/request", methods=['POST'])
def request_recipe():
    try:
        category = request.form.get("mealType")
        instructions = request.form.get("request")
        request_data = RecipeDimension(category=category, recipe_name=instructions,
                                       status="uncompleted", user_id=session["user_id"])
        db.session.add(request_data)
        db.session.commit()
        recipes = RecipeDimension.query.all()
        return render_template('Main.html', recipes=recipes)
    except KeyError:
        return redirect(url_for('auth.login'))


@BP.route("/NoneLogin", methods=['GET', 'POST'])
def none_login():
    try:
        user_id = session["user_id"]
        return render_template("Main.html", popup_form='block')
    except KeyError:
        return render_template("Main.html", none_login_form='block')
