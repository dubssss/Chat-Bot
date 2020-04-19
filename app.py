from flask import Flask, render_template, request, session
import sendemailmsg
app = Flask(__name__)
app.secret_key="seckey"

@app.route('/', methods=["GET"])
def home():
    return render_template('login.html')

@app.route('/uservalid', methods=["POST", "GET"])
def uservalid():
    if 'loggedin' in session:
        render_template('chatbot.html')
    username = request.form.get("username")
    password = request.form.get("password")
    if (username == "anubha" and password == "dubey"):
        session['loggedin']=username
        return render_template('chatbot.html')
    else:
        return "<h1>Incorrect Credentials</h1>"

@app.route('/processreply', methods=["POST", "GET"])
def processreply():
    jobject = request.json
    msg = (jobject['msg'])
    msg = msg.upper().rstrip()
    botreply = str

    if (msg == "HI" or msg == "HELLO" or msg == "HEY"):
        return "Hello, please choose from one of the following: <br> 1. Send ExcelA <br>2. Send ExcelB "
    elif (msg == "1"):
        botreply="Received request for option 1. Thank you"
        return "Email sent for option 1",sendemailmsg.sendemailmsg("1")
    elif (msg == "2"):
        botreply="Received response for option 2. Thank you"
        return "Email sent for option 2",sendemailmsg.sendemailmsg("2")
    else:
        botreply = "I don't understand this. Try again :) <br>Please choose from one of the following: <br>1. Send ExcelA <br>2. Send ExcelB"
    return botreply

@app.route('/logout',methods=["GET"])
def logout():
    if 'loggedin' in session:
        session.pop('loggedin', None)
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
