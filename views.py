from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)

# view in this instance is a Blueprint

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/customized")
def customized():
    return render_template("customized.html")

@views.route("/merchandise")
def merchandise():
    return render_template("merchandise.html")

@views.route("/retrogaming")
def retrogaming():
    return render_template("retrogaming.html")

@views.route("/visit")
def visit():
    return render_template("visit.html")

