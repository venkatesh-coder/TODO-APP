from flask import Flask, render_template
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)


# Configure db
db = yaml.load(open('db.yaml'))
app.config["MYSQL_HOST"] = db['mysql_host'] 
app.config["MYSQL_USER"] = db['mysql_user']
app.config["MYSQL_PASSWORD"] = db['mysql_password']
app.config["MYSQL_DB"] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    data = cur.execute("SELECT * FROM tasks")
    if data > 0:
        users = cur.fetchall()
        return render_template("index.html", users=users)
    return 'No users'
if __name__ == '__main__':
    app.run(debug=True)
