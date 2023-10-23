from flask import Flask, render_template, request

app = Flask(__name__)


    
def check_password_strength(password):
    # Initialize strength score
    strength = 0

    # Check password length
    if len(password) > 8:
        strength += 2
    elif 6 <= len(password) <= 8:
        strength += 1

    # Check for uppercase and lowercase letters
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        strength += 2

    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1

    # Check for special characters
    special_chars = "!@#$%^&*()_+[]{};:,.<>?/\\"
    if any(char in special_chars for char in password):
        strength += 2

    # Determine password strength level
    if strength >= 5:
        return "Strong"
    elif strength >= 3:
        return "Medium"
    else:
        return "Weak"







@app.route('/', methods=['GET', 'POST'])
def index():
    strength_level = None
    if request.method == 'POST':
        password = request.form['password']
        strength_level = check_password_strength(password)
    return render_template('index.html', strength_level=strength_level)

if __name__ == '__main__':
    app.run(debug=True)
