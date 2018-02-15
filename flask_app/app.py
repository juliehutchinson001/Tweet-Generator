#import flask class
from flask import Flask
# import 

#created an instance of this class
app = Flask(__name__)
app.config['DEBUG'] = True

#This is a route decorator that tells Flask the url to execute our function
@app.route('/')
def hello_world():
    return 'Hello, World!'