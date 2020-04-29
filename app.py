from flask import Flask, render_template, request, session
import sendemailmsg
import requesterlist 

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
    authorised_req={}
    authorised_req=requesterlist.getdata()
    
    if authorised_req.get(username,0) == password:
        session['loggedin']=username
        return render_template('chatbot.html')
    else:
        return "<h1>Incorrect Credentials. Try again :) </h1>"
    '''if (username == "anubha" and password == "dubey"):
        session['loggedin']=username
        return render_template('chatbot.html')
    else:
        return "<h1>Incorrect Credentials</h1>" '''

@app.route('/processreply', methods=["POST", "GET"])
def processreply():
    jobject = request.json
    msg = (jobject['msg'])
    msg = msg.upper().rstrip()


    if (msg == "HI" or msg == "HELLO" or msg == "HEY"):
        return "Hello, please choose from one of the following: <br><br> 1. Send Excel_1 <br>2. Send Excel_2 "
    elif (msg == "1"):
        return "Email sent for option 1",sendemailmsg.sendemailmsg("1")
    elif (msg == "2"):
        return "Email sent for option 2",sendemailmsg.sendemailmsg("2")
    else:
        return "I don't understand this. Try again :) <br><br>Please choose from one of the following: <br>1. Send Excel_1 <br>2. Send Excel_2"


@app.route('/logout',methods=["GET"])
def logout():
    if 'loggedin' in session:
        session.pop('loggedin', None)
        return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
