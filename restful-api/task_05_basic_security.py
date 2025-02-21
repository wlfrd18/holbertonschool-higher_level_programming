from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de la clé secrète pour JWT
app.config['SECRET_KEY'] = 'votre_clé_secrète'

# Initialisation de l'authentification de base et JWT
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Utilisateur fictif pour l'exemple
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Fonction d'authentification de base
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

# Route protégée avec authentification de base
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted")

# Route de connexion pour obtenir un token JWT
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Création d'un token JWT
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Route protégée avec authentification JWT
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted", user=current_user)

# Route protégée basée sur le rôle (administrateur)
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]['role'] != 'admin':
        return jsonify(error="Admin access required"), 403
    return jsonify(message="Admin Access: Granted")

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)

