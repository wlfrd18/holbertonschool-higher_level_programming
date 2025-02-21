from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for JWT encoding/decoding
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the Basic Authentication and JWT extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Initialize an empty dictionary to store users
users = {}

# Basic Authentication: Verify the username and password
@auth.verify_password
def verify_password(username, password):
    if username in users:
        print(f"User {username} found in users dictionary.")
        if check_password_hash(users[username]['password'], password):
            return username  # Return the username if credentials are valid
        else:
            print("Incorrect password.")
    else:
        print(f"User {username} not found.")
    return None

# Route protected by Basic Authentication
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    # This route is protected by basic authentication
    return jsonify(message="Basic Auth: Access Granted")

# Route for login to generate a JWT token
@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the request JSON body
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    # Validate credentials
    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401  # Return 401 if credentials are invalid
    
    # Generate a JWT token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Route for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    # Get the user data from the JSON request body
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    role = request.json.get('role', 'user')  # Default role is 'user'

    # Check if the username is provided
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if the password is provided
    if not password:
        return jsonify({"error": "Password is required"}), 400

    # Hash the password before storing it
    hashed_password = generate_password_hash(password)

    # Add the user to the users dictionary
    users[username] = {"username": username, "password": hashed_password, "role": role}
    
    return jsonify({"message": "User added", "user": users[username]}), 201

# Route protected by JWT Authentication
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    # Get the identity (username) from the current JWT token
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted")

# Route protected by JWT Authentication and Role-based access control
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    # Get the identity (username) from the current JWT token
    current_user = get_jwt_identity()
    
    # Check if the current user has an 'admin' role
    if users[current_user]['role'] != 'admin':
        return jsonify(error="Admin access required"), 403  # Return 403 if user is not an admin
    return jsonify(message="Admin Access: Granted")

# Custom error handlers for different JWT errors

# Handler for missing or invalid token
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

# Handler for invalid token
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

# Handler for expired token
@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# Handler for revoked token
@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

# Handler for fresh token requirement
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)


