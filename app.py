from flask import Flask,flash,render_template,url_for,request,session,g,redirect
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()