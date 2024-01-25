# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

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
# ‘/hello’ URL is bound with hello_world() function.

@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

# create a dynamic route
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

# create a dynamic route with a default value
@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()