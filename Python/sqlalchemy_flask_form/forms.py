from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from flask_sqlalchemy import SQLAlchemy
from wtforms import validators, ValidationError
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_mail import Mail, Message
import time

app = Flask(__name__)
app.secret_key = 'development key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
db = SQLAlchemy(app)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kuldeep.tb.mali@gmail.com'
app.config['MAIL_PASSWORD'] = '@kuldeep102'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

class ContactForm(FlaskForm):
    name = TextField("Name Of Student", [validators.Required("Please enter your name.")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField("Address")

    email = TextField("Email", [validators.Required("Please enter your email address."),validators.Email("Please enter your email address.")])

    Age = IntegerField("age")
    language = SelectField('Languages', choices=[('cpp', 'C++'),('py', 'Python')])
    submit = SubmitField("Send")



class students(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100))
   Genger = db.Column(db.String(50))
   Address = db.Column(db.String(200))
   email= db.Column(db.String(200))
   Age = db.Column(db.Integer)
   language = db.Column(db.String(200))



   def __init__(self, name, Genger, Address, email, Age,language):

       self.name = name
       self.Genger = Genger
       self.Address = Address
       self.Age = Age
       self.language = language
       self.email = email