from flask import Flask
from flask import render_template, request, redirect, url_for, send_from_directory, jsonify, session
from datetime import datetime
import os

from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

from dotenv import load_dotenv
from flask_cors import CORS

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = 'S3cr3t0'

CORS(app)
mysql = MySQL()

NOMBRE_TABLA = 'empleados'

# Auth

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        conn = mysql.connect()
        cursor = conn.cursor(DictCursor)

        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        sql = 'INSERT INTO usuarios (email, password) VALUES (%s, %s)'
        values = [email, password]    

        cursor.execute(sql, values)

        conn.commit()

        return redirect(url_for('index'))
    else:
        return render_template('auth/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = mysql.connect()
        cursor = conn.cursor(DictCursor)

        email = request.form['email']
        password = request.form['password']
        
        sql = 'SELECT * FROM usuarios WHERE email = %s'
        values = [email]    

        cursor.execute(sql, values)
        usuario = cursor.fetchone()

        print(usuario)

        if usuario == None:
            print('El usuario es incorrecto')
        elif check_password_hash(usuario['password'], password) == False:
            print('La contraseña es incorrecta')
        else:
            session['id'] = usuario['id']

        # conn.commit()

        return redirect(url_for('index'))
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    if 'id' in session:
        session.pop('id')

    return redirect(url_for('index'))

@app.route('/perfil')
def perfil():
    if 'id' not in session:
        return redirect(url_for('login'))

    return 'Perfil'

# API CRUD

@app.route('/api/empleados')
def api_empleados():
    conn = mysql.connect()
    cursor = conn.cursor(DictCursor)

    cursor.execute('SELECT * FROM empleados')
    empleados = cursor.fetchall()

    # print(empleados)

    return jsonify(empleados)

# Web CRUD

@app.route('/uploads/<path:imagen>')
def uploads(imagen):
    return send_from_directory(os.path.join('../uploads'), imagen)

@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor(DictCursor)

    cursor.execute('SELECT * FROM empleados')
    empleados = cursor.fetchall()

    # conn.commit()

    print(empleados)

    mensaje = 'Listado de empleados'
    return render_template('index.html', mensaje=mensaje, empleados=empleados)

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

    if request.files['imagen'].filename != '':
        imagen = request.files['imagen']

        now = datetime.now()
        time = now.strftime('%Y%m%d%H%M%S')

        nombre_imagen = time + '_' + imagen.filename

        imagen.save('uploads/' + nombre_imagen)

        sql = 'INSERT INTO empleados (nombre, correo, imagen) VALUES (%s, %s, %s)'
        values = [nombre, correo, nombre_imagen]
    else:
        sql = 'INSERT INTO empleados (nombre, correo) VALUES (%s, %s)'
        values = [nombre, correo]    

    cursor.execute(sql, values)

    conn.commit()

    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    sql = 'SELECT * FROM empleados WHERE id = %s'
    values = [id]

    conn = mysql.connect()
    cursor = conn.cursor(DictCursor)

    cursor.execute(sql, values)
    empleado = cursor.fetchone()

    # print(empleado)

    return render_template('edit.html', empleado=empleado)

@app.route('/update', methods=['POST'])
def update():
    print(request.form)
    print(request.files)

    conn = mysql.connect()
    cursor = conn.cursor(DictCursor)

    id = request.form['id']
    nombre = request.form['nombre']
    correo = request.form['email']

    if request.files['imagen'].filename != '':
        sql = 'SELECT imagen FROM empleados WHERE id = %s'
        values = [id]

        cursor.execute(sql, values)
        empleado = cursor.fetchone()

        if empleado['imagen'] != None:
            try:
                os.remove(os.path.join('uploads', empleado['imagen']))
            except:
                pass

        imagen = request.files['imagen']

        now = datetime.now()
        time = now.strftime('%Y%m%d%H%M%S')

        nombre_imagen = time + '_' + imagen.filename

        imagen.save('uploads/' + nombre_imagen)

        sql = 'UPDATE empleados SET nombre = %s, correo = %s, imagen = %s WHERE id = %s'
        values = [nombre, correo, nombre_imagen, id]
    else:
        sql = 'UPDATE empleados SET nombre = %s, correo = %s WHERE id = %s'
        values = [nombre, correo, id]

    cursor.execute(sql, values)

    conn.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = mysql.connect()
    cursor = conn.cursor()

    sql = 'SELECT imagen FROM empleados WHERE id = %s'
    values = [id]

    cursor.execute(sql, values)
    empleado = cursor.fetchone()

    if empleado[0] != None:
        try:
            os.remove(os.path.join('uploads', empleado[0]))
        except:
            pass

    sql = 'DELETE FROM empleados WHERE id = %s'
    values = [id]

    cursor.execute(sql, values)

    conn.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    load_dotenv()

    app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASS')
    app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DB')

    mysql.init_app(app)

    app.run(debug=True)