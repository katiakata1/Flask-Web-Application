from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)

app.config['MYSQL_HOST'] = 'database-2.cqeuduzjsbcl.eu-west-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Russia#1'
app.config['MYSQL_DB'] = 'learning'
mysql = MySQL(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # supplies = db.relationship('Supplies', backref='user')

    def __repr__(self):
        return '<Name %r>' % self.username

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     description = db.Column(db.String(200), nullable=False)

class Supplies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(200), nullable=False)
    reasons_for_request = db.Column(db.String(200))
    quantity = db.Column(db.Integer, nullable=False)
    date_requested = db.Column(db.DateTime, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return '<Item %r>' % self.id





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



@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    itemname = request.form.get('item_name')
    reasons = request.form.get('reasons_for_request')
    quantity = request.form.get('item_quantity')

    try: 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO supplies(item_name, reasons_for_request, quantity) VALUES (%s, %s, %s)" , (itemname, reasons, quantity))
        mysql.connection.commit()
        cur.close()
        return redirect('/welcome')
        
    except: 
        return render_template('welcome.html', item_name = itemname, reasons_for_request = reasons, item_quantity = quantity)

    # tasks = Supplies.query.order_by(Supplies.date_requested).all()  
    # return render_template('welcome.html', item_name = itemname)
    




@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Supplies.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deliting your task'



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Supplies.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except: 
            return 'There was an issue updating yout task'
    else: 
        return render_template('update.html', task=task)

if __name__=='__main__':
    app.run(debug=True)




# @app.route('/logout')
# def logout():
#     session.pop('logged_in', None)
#     flash('You were just logged out!')
#     return redirect(url_for('home'))








        # if request.method == 'POST': #if 'post' happends do thi
    #     user_name = request.form['name'] #take the value put in name input and store in a user_name variable
    #     new_user = User(username=user_name) #take the user_name value and put it in a User db

    #     # Push to Database
    #     try:
    #          db.session.add(new_user)
    #          db.session.commit()
    #          return redirect ('/login')
    #     except:
    #          return "There was an error adding your name"

    # else:
    #     return render_template('login.html')