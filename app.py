from flask import Flask,flash,render_template,url_for,request,session,g,redirect
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods = ['POST'])
def loginfun():
    return render_template('/home/gopal/Desktop/hack_flip/ML001_MOVIE_RECOMMENDATION_ENGINE/templates/login.html')    

app.run(debug=True)