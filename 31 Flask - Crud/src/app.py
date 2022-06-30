from flask import Flask
from flask import render_template, request, redirect, url_for
from datetime import datetime

from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'empleados'

mysql.init_app(app)

@app.route('/')
def index():
    # conn = mysql.connect()
    # cursor = conn.cursor()

    # cursor.execute('SELECT * FROM city LIMIT 10')
    # city = cursor.fetchall()

    # print(city)

    mensaje = 'Hola Flask'
    return render_template('index.html', mensaje=mensaje)

@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')

# API
# GET, POST, PUT, PATCH, DELETE

@app.route('/store', methods=['POST'])
def store():
    print(request.form)
    print(request.files)

    conn = mysql.connect()
    cursor = conn.cursor()

    nombre = request.form['nombre']
    correo = request.form['email']

    imagen = request.files['imagen']

    now = datetime.now()
    time = now.strftime('%Y%m%d%H%M%S')

    nombre_imagen = time + '_' + imagen.filename

    imagen.save('uploads/' + nombre_imagen)

    sql = 'INSERT INTO empleados (nombre, correo, imagen) VALUES (%s, %s, %s)'
    values = [nombre, correo, nombre_imagen]

    cursor.execute(sql, values)

    conn.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)