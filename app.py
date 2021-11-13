from flask import Flask,flash,render_template,url_for,request,session,g,redirect
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'gopal'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'flip'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()

#cursor.execute("SELECT * from User")
#data = cursor.fetchone()

@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/login',methods = ['POST'])
#def loginfun():
#    return render_template('/home/gopal/Desktop/hack_flip/ML001_MOVIE_RECOMMENDATION_ENGINE/templates/login.html')    

@app.route('/successauth')
def successauth():
    return "Login Successful!"

@app.route('/failedauth')
def failedauth():
    return "Either Email-id or password is incorrect!"    

@app.route('/loginuser', methods = ['POST'])
def loginuser():
    email_id = request.form['userEmailAdd']
    password = request.form['password']

    cursor.execute('SELECT email, password from user')
    results = cursor.fetchall()

    for row in results:
        if email_id==row[0] and password==row[1]:
            return redirect(url_for('successauth'))

    return redirect(url_for('failedauth'))        

@app.route('/login',methods = ['POST'])
def login():
    # if 'user' in session:
    #     return render_template('home-sani.html',redic=session['userData'])
    return render_template('login.html')

@app.route('/success<fname><lname>')
def success(fname, lname):
    return 'Welcome '+fname + ' ' + lname

@app.route('/registeruser', methods = ['POST'])
def registeruser():
    first_name = request.form['userFName']
    last_name = request.form['userLName']
    email_id = request.form['userEmailAdd']
    password = request.form['password']
    call_number = request.form['userContact']

    query = 'INSERT INTO user(fname, lname, email, password, mobile_number) values (%s,%s,%s,%s,%s)'
    value = (first_name,last_name,email_id,password,call_number)
    cursor.execute(query,value)

    conn.commit() 
    return redirect(url_for('success',fname = first_name, lname = last_name))


@app.route('/register')
def register():
    return render_template('register.html')


# if __name__ == '__main__':
app.run(debug=True)