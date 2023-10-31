from flask import Flask, render_template, request
import re
import string
import hashlib

app= Flask(__name__, static_folder='static')

# Función para verificar la contraseña
def is_password_safe(password):
    # Check if password meets complexity requirements
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*()\-_=+{};:,<.>/?\\|~]', password):
        return False
    
    return True

# Función para hashear la contraseña
def hash_password(password):
     # Encode the password string before hashing
    encoded_password = password.encode('utf-8')

    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the encoded password
    sha256.update(encoded_password)

    # Get the hexadecimal representation of the hash
    hashed_password = sha256.hexdigest()
    return hashed_password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        if is_password_safe(password):
            hashed_password = hash_password(password)
            return render_template('index.html', hashed_password=hashed_password)
        else:
            return render_template('index.html', error="Password not secure")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)