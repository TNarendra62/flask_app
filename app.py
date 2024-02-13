from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (replace this with a proper user authentication system)
users = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return f'Welcome, {username}!'
    else:
        return 'Invalid login credentials. Please try again.'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
