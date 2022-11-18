from flask import Flask, render_template

import re



# from gevent.pywsgi import WSGIServer
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def page():
 return render_template('Dashboard.html')



@app.route("/about")  
def about():
  return render_template('about.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/logging')
def logging():
  return render_template('logging.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

