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

@app.route('/login',methods = ['POST'])
def login():
    # if 'user' in session:
    #     return render_template('home-sani.html',redic=session['userData'])
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

# if __name__ == '__main__':
app.run(debug=True)