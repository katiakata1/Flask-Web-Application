import MySQLdb
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/project.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'secret_key'
# db = SQLAlchemy(app)

app.config['MYSQL_HOST'] = 'database-2.cqeuduzjsbcl.eu-west-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Russia#1'
app.config['MYSQL_DB'] = 'learning'
mysql = MySQL(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(30), nullable=False)
#     password = db.Column(db.String(30), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#     # supplies = db.relationship('Supplies', backref='user')

#     def __repr__(self):
#         return '<Name %r>' % self.username

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     description = db.Column(db.String(200), nullable=False)

# class Supplies(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     item_name = db.Column(db.String(200), nullable=False)
#     reasons_for_request = db.Column(db.String(200))
#     quantity = db.Column(db.Integer, nullable=False)
#     date_requested = db.Column(db.DateTime, default=datetime.utcnow)
#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


#     def __repr__(self):
#         return '<Item %r>' % self.id

@app.route('/', methods = ['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    try: 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()
        return redirect('/welcome')
    except:
        return redirect('/welcome')


@app.route('/supplies', methods=['POST'])
def supplies():
    cur = mysql.connection.cursor()

    try:
        itemname = request.form.get('item_name')
        reasons = request.form.get('reasons_for_request')
        quantity = int(request.form.get('quantity'))

        cur.execute("INSERT INTO supplies(item_name, reason_for_request, quantity) VALUES (%s, %s, %s)" , (itemname, reasons, quantity))
        mysql.connection.commit()
        return render_template('welcome.html')
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        return e
    finally:
        cur.close()

@app.route('/welcome', methods=['GET'])
def welcome():
    return render_template('welcome.html')

# @app.route('/delete/<int:id>')
# def delete(id):
#     # task_to_delete = Supplies.query.get_or_404(id)

#     try:
#         # db.session.delete(task_to_delete)
#         # db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deliting your task'



# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Supplies.query.get_or_404(id)

#     if request.method == 'POST':
#         task.content = request.form['content']

#         try:
#             db.session.commit()
#             return redirect('/')
#         except: 
#             return 'There was an issue updating yout task'
#     else: 
#         return render_template('update.html', task=task)
app.run(debug=True)
