from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    paswword = db.Column(db.String(30), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.id


@app.route('/login', methods = ['GET', 'POST'])

def login():
    error = None
    if request.method == 'POST':


        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid Credentials. Please try again"
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('welcome'))
    return render_template('login.html', error = error)


@app.route('/welcome', methods=['GET', 'Post'])
def welcome():
    return render_template('welcome.html')
 

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')




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