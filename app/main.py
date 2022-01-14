from flask import Flask
from flask import request

app = Flask(__name__)

last_info = "There were no info yet"
operation = 0
with open("app/operation.txt", 'r') as fin:
    operation = fin.readline()
    operation = operation.rstrip()

def change_info(inf):
    global last_info 
    last_info= inf

@app.route("/", methods = ['POST', 'GET'])
def new_info():
    global last_info
    global operation
    if request.method == 'POST':
        if request.form['switch_option'] == 'Do Something':
            if operation == '1':
                operation = '2'
            else:
                operation = '1'
            with open("app/operation.txt", 'w') as fout:
                fout.write(operation)
        
        else:
            last_info= request.args.get("info",'')
    return last_info+"""<form method="post"><input type="submit" name="switch_option" value="Do Something"></form>"""



@app.route("/operation", methods = ['GET'])
def operation(): 
    global operation 
    return operation


