# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
import sqlite3

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with welcome() function.
def welcome():
    return "Welcome to the Flask Web Server!"

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

    @app.route('/login', methods=['POST'])
    def login():
        username = request.form['username']
        password = request.form['password']
        
        # Insecure: Directly concatenating user input into SQL query
        # Vulnerable to SQL injection attacks
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
        cursor.execute(query)
        result = cursor.fetchone()
        
        # Rest of the login logic
        ...


#an example of an insecure connection to a database
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Insecure: Directly concatenating user input into SQL query
    # Vulnerable to SQL injection attacks
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    
    # Rest of the login logic
    ...
