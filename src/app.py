from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from keys import Key
from newuser import insert_user

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': Key.host,
    'user': Key.user,
    'password': Key.password,
    'database': 'movierecs'
}

# Function to verify user credentials
def verify_user(email, password):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "SELECT * FROM user WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user is not None

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        password = request.form['password']

        # Insert new user into the database
        if insert_user(email, first_name, last_name, password):
            return redirect('/login')  # Redirect to login page on successful signup
        else:
            return "Failed to create user. Please try again."  # Error message if signup fails

    return render_template('signup.html')

# Route to render the login page
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if verify_user(email, password):
            return redirect('/welcome')
        else: 
            return "Failed credentials"

@app.route('/welcome')
def welcome():
    return "Welcome to the dashboard!"


if __name__ == '__main__':
    app.run(debug=True)
