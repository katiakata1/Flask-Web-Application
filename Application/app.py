import MySQLdb
from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


app.config['MYSQL_HOST'] = 'database-2.cqeuduzjsbcl.eu-west-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Russia#1'
app.config['MYSQL_DB'] = 'learning'
mysql = MySQL(app)


@app.route('/', methods = ['GET'])
def dashboard():
    return render_template('dashboard.html')


#Enter the credentials
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    try: 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()
        return redirect('/supplies')
    except:
        return redirect('/supplies')


# See and Post Item
@app.route('/supplies', methods=['GET', 'POST'])
def supplies():
    if request.method == 'POST':
        cur = mysql.connection.cursor()

        try:
            itemname = request.form.get('item_name')
            reasons = request.form.get('reasons_for_request')
            quantity = int(request.form.get('quantity'))

            cur.execute("INSERT INTO supplies(item_name, reason_for_request, quantity) VALUES (%s, %s, %s)" , (itemname, reasons, quantity))
            mysql.connection.commit()
            return redirect('/supplies')
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print(e)
            return e
        finally:
            cur.close()
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM supplies")
        data = cur.fetchall()
        return render_template('supplies.html', results = data)


# Delete Item
@app.route('/delete_item/<int:id>', methods=['GET', 'POST', 'DELETE'])
def delete_item(id):
    # Create cursor
    cur = mysql.connection.cursor() 

    # Execute
    cur.execute("DELETE FROM supplies WHERE id = %s", [id])

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    return redirect(url_for('supplies'))


#View Item
@app.route('/item/<id>', methods=['GET'])
def view_item(id):
    item_id = int(id)
    cur = mysql.connection.cursor()
    try:
        query = "SELECT * from supplies WHERE id=%s"
        cur.execute(query, [item_id])
        item_found = cur.fetchall()[0]
        return render_template('item.html', item = item_found)
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        print(e)
        return e
    finally:
        cur.close()



#Update Item
@app.route('/item/<int:id>', methods=['POST'])
def update_item(id):
    itemname = request.form.get('item_name', False)
    reasons = request.form.get('reasons_for_request', False)
    quantity = int(request.form.get('quantity', False))
    
    cur = mysql.connection.cursor()
    cur.execute("""
            UPDATE supplies
            SET item_name=%s, reason_for_request=%s, quantity=%s WHERE id = %s 
        # """, [itemname, reasons, quantity, id])

    mysql.connection.commit()
    cur.close()
    return redirect(url_for('supplies'))



if __name__ == "__main__":
    app.run(debug=True)