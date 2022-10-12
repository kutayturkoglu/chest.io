from flask import render_template, request
from matplotlib import use
from app import app, mysql
from flask_sqlalchemy import SQLAlchemy
from datetime import date

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

@app.route('/redirect', methods=(['GET','POST']))
def redirect():
    username=request.form['user_name']
    password=request.form['user_pw']
    email=request.form['user_email']
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO User(user_name,user_email,user_pw) VALUES(%s,%s,%s)", (username,email,password))
    mysql.connection.commit()
    cur.close()
    return render_template('redirect.html')