from flask import Flask
from flask import render_template 

from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'world'

mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM city LIMIT 10')
    city = cursor.fetchall()

    print(city)

    mensaje = 'Hola Flask'
    return render_template('index.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)