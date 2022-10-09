from flask import render_template
from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI']='mysql://kutay:448255@localhost/chest'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personal', methods=(['GET','POST']))
def personal():
    return render_template('personal.html')

@app.route('/blog', methods=(['GET','POST']))
def blog():
    return render_template('blog.html')

@app.route('/reminder', methods=(['GET','POST']))
def reminder():
    return render_template('reminder.html')

@app.route('/diary', methods=(['GET','POST']))
def diary():
    return render_template('diary.html')

@app.route('/signup', methods=(['GET','POST']))
def signup():
    return render_template('signup.html')