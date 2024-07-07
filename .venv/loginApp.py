from flask import Flask, request, jsonify
import mysql.connector
import google.auth.transport.requests
import google.oauth2.id_token

app = Flask(__name__)

# Configura la conexión a la base de datos
#db_config = {
#    'user': 'tu_usuario',
#    'password': 'tu_contraseña',
#    'host': 'tu_host',
#    'database': 'tu_base_de_datos'
#}

# Ruta para validar el inicio de sesión
@app.route('/validate-login', methods=['POST'])
def validate_login():
    data = request.json
    username = data['username']
    password = data['password']

    #connection = mysql.connector.connect(**db_config)
    #cursor = connection.cursor()
    #cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = %s AND contrasena = %s", (username, password))
    #user = cursor.fetchone()
    #cursor.close()
    #connection.close()

    #if user:
    return jsonify(success=True, message="Login successful")
    #else:
    #    return jsonify(success=False, message="Invalid username or password")

# Ruta para validar el inicio de sesión con Google
@app.route('/validate-google-login', methods=['POST'])
def validate_google_login():
    data = request.json
    id_token = data['id_token']

    try:
        # Verifica el token de Google
        request_adapter = google.auth.transport.requests.Request()
        idinfo = google.oauth2.id_token.verify_oauth2_token(id_token, request_adapter, 'TU_CLIENTE_ID')

        email = idinfo['email']

        # Conecta a la base de datos para buscar al usuario
        #connection = mysql.connector.connect(**db_config)
        #cursor = connection.cursor()
        #cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        #user = cursor.fetchone()
        #cursor.close()
        #connection.close()

        #if user:
        return jsonify(success=True, message="Google login successful")
        #else:
        #    return jsonify(success=False, message="User not found in database")

    except ValueError as e:
        return jsonify(success=False, message=str(e))

if __name__ == '__main__':
    app.run(debug=True)
