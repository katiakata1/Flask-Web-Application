from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
app.run(debug=True)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/project.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SECRET_KEY'] = 'secret_key'
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



@app.route('/welcome', methods=['GET'])
def welcome():
    itemname = request.form.get('item_name')
    reasons = request.form.get('reasons_for_request')
    quantity = request.form.get('item_quantity')
    # items = Supplies.query.all()  

    try: 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO supplies(item_name, reasons_for_request, quantity) VALUES (%s, %s, %s)" , (itemname, reasons, quantity))
        mysql.connection.commit()
        # cur.execute("SELECT item_name AS item_name, reasons_for_request AS reasons_for_request, quantity AS item_quantity FROM supplies;")
        # data = cur.fetchall()
        # print(data)
        cur.close()
        return redirect('/welcome')
        
    except:
        return redirect('/welcome')
        # items = Supplies.query.all()  
        # return render_template('welcome.html', items = items)

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route("/site-map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))



    # tasks = Supplies.query.order_by(Supplies.date_requested).all()  
    # return render_template('welcome.html', item_name = itemname)
    




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