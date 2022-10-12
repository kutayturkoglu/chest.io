from flask import render_template, request
from matplotlib import use
from app import app, mysql
from datetime import date

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personal', methods=(['GET','POST']))
def personal():
    email=request.form['email']
    password=request.form['password']
    cur=mysql.connection.cursor()
    try:
        cur.execute("SELECT user_pw FROM User WHERE user_email=%s",(email,))
        pw=cur.execute("SELECT user_pw FROM User WHERE user_email=%s",(email,))
        pw=cur.fetchall()
        print(pw[0][0])
        if(pw[0][0]==password):
            username=cur.execute("SELECT user_name FROM User WHERE user_email=%s",(email,))
            username=cur.fetchall()
            return render_template('personal.html', user_name=username[0][0])
        else:
            hed='<h1>This is the wrong password'
            return (hed)
    except:
        hed='<h1>This email adress is not registered.'
        return (hed) 
    

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
    try:
        cur.execute("INSERT INTO User(user_name) VALUES(%s)", (username))
    except Exception as e:
        hed='<h1>This user name is taken before'
        return (hed) 
    try:
        cur.execute("INSERT INTO User(user_email) VALUES(%s)", (email))
    except Exception as e:
        hed='<h1>This email is used before'
        return (hed) 
    
    cur.execute("INSERT INTO User(user_pw) VALUES(%s)", (password))
    mysql.connection.commit()
    cur.close()
    return render_template('redirect.html')