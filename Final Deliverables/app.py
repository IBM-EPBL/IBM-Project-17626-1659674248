from flask import Flask, render_template, request
from sendmail import sendgridmail
from sendmail2 import sendgridmail
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
  if request.method == "POST":
       # getting input with name = fname in HTML form
       floatinglimit = request.form.get("form-control")
       # getting input with name = lname in HTML form
       floatingincome = request.form.get("form-control")
       
       floatingexpense = request.form.get("form-control")
      
  if (floatingincome-floatingexpense>=floatinglimit):
      return sendgridmail("hello","roshinisri1234@gmail.com")

  
  return render_template('logging.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

