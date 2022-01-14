from flask import Flask
from flask import request

app = Flask(__name__)

last_info = "There were no info yet"
def change_info(inf):
    global last_info 
    last_info= inf

@app.route("/", methods = ['POST', 'GET'])
def new_info():
    global last_info
    if request.method == 'POST':
        last_info= request.args.get("info",'')
    return last_info



@app.route("/operation", methods = ['GET'])
def operation():  
    return "1"


