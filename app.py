from flask import Flask,flash,render_template,url_for,request,session,g,redirect,session
from flaskext.mysql import MySQL
import os
import random
from util import nearby

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


@app.route('/home', methods = ['POST','GET'])
def home():
    if 'user' in session:
        restName,total,rating = nearby()
        return render_template('home.html',name = session['name'],restName = restName,total=total,row = int(total/5)+1,rating = rating, dic = ["static/image/r1.jpg","static/image/r2.jpg","static/image/r3.jpg","static/image/r4.jpg","static/image/r5.jpg",])


    email_id = request.form['userEmailAdd']
    password = request.form['password']
    
    cursor.execute('SELECT fname, email, password from user')
    results = cursor.fetchall()

    for row in results:
        if email_id==row[1] and password==row[2]:
            restName,total,rating = nearby()
            session['user'] = email_id
            session['name'] = row[0]
            print(row[0])
            return render_template('home.html',name = row[0],restName = restName,total=total,row = int(total/5)+1,rating = rating, dic = ["static/image/r1.jpg","static/image/r2.jpg","static/image/r3.jpg","static/image/r4.jpg","static/image/r5.jpg",])

    return  render_template('login.html',perror = "Either Email-id or password is incorrect!")

@app.route('/bestseller')
def bestseller():
    restName,total,rating = nearby()
    name = session['name']
    index = random.sample(range(total),5)
    rn = []
    rat = []
    for r in index:
        rn.append(restName[r])
        rat.append(rating[r])
    return render_template('home.html',name = name,restName = rn,total=5,row = 1,rating = rat, dic = ["static/image/r1.jpg","static/image/r2.jpg","static/image/r3.jpg","static/image/r4.jpg","static/image/r5.jpg",])



@app.route('/myfav')
def myfav():
    restName,total,rating = nearby()
    name = session['name']
    index = random.sample(range(total),5)
    rn = []
    rat = []
    for r in index:
        rn.append(restName[r])
        rat.append(rating[r])
    return render_template('home.html',name = name,restName = rn,total=5,row = 1,rating = rat, dic = ["static/image/r1.jpg","static/image/r2.jpg","static/image/r3.jpg","static/image/r4.jpg","static/image/r5.jpg",])


@app.route('/restaurant')
def restaurant():
    name = request.form['restName']
    cursor.execute("Select * from " + name)
    results = cursor.fetchall()
    for row in results:
        print(row)

@app.route('/login',methods=['POST'])
def login():
    # if 'user' in session:
    #     return render_template('home-sani.html',redic=session['userData'])
    return render_template('login.html')




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
    restName,total,rating = nearby()
    session['user'] = email_id
    session['name'] = first_name
            
    return render_template('home.html',name = first_name,restName = restName,total=total,row = int(total/5)+1,rating = rating, dic = ["static/image/r1.jpg","static/image/r2.jpg","static/image/r3.jpg","static/image/r4.jpg","static/image/r5.jpg",])


@app.route('/register')
def register():
    return render_template('register.html')
     

@app.route('/menu',methods=['POST'])
def menu():
    name = request.form['restName']
    cursor.execute("Select * from food_item")
    results = cursor.fetchall()
    index = random.sample(range(23),6)
    item = []
    for r in index:
        item.append([results[r][1],results[r][2]])
    
    return render_template('menu.html',name=session['name'],item = item)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/logout')
def logout():
    if 'user' in session:
        session.clear()
    return render_template('index.html')




# if __name__ == '__main__':
app.run(debug=True)