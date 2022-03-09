from flask import Blueprint, render_template
from forms.registerForm import RegisterForm

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():
    return render_template("home.html")


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/register")
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)


@auth.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
