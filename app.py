from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

# Function to generate the secure key based on the type selected
def generate_secure_key(length=32, key_type='mixed'):
    if key_type == 'hex':
        return secrets.token_hex(length // 2)  # Hex generates twice as many characters
    elif key_type == 'base64':
        return secrets.token_urlsafe(length)
    elif key_type == 'alphanumeric':
        characters = string.ascii_letters + string.digits
    else:  # Mixed (includes special characters)
        characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def home():
    generated_key = None
    if request.method == 'POST':
        key_length = int(request.form['length'])
        key_type = request.form['key_type']  # Get key type from the form
        generated_key = generate_secure_key(key_length, key_type)
    return render_template('index.html', generated_key=generated_key)

if __name__ == "__main__":
    app.run(debug=True)
