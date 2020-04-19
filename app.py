from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/', methods=["GET"])
def home():
    return render_template('login.html')

@app.route('/uservalid',methods=["POST","GET"])
def uservalid():
    username=request.form.get("username")
    password=request.form.get("password")
    if (username=="anubha" and password=="dubey"):
        return render_template('chatbot.html')
    else:
        return "<h1>Incorect Credentials</h1>"

@app.route('/processreply', methods=["POST","GET"])
def processreply():
    jobject = request.json
    msg=(jobject['msg'])
    msg=msg.upper().rstrip()
    botreply=str

    if (msg== "HI" or msg=="HELLO" or msg=="HEY"):
        botreply="Hello, please choose from one of the following: <br> 1. Send ExcelA <br>2. Send ExcelB"
    elif (msg=="1"):
        botreply="You selected option 1.<br>Thank you"
    elif (msg=="2"):
        botreply="You selected option 2.<br>Thank you"
    else:
        botreply="I don't understand this. Try again :) <br>Please choose from one of the following: <br>1. Send ExcelA <br>2. Send ExcelB"
    return botreply

    

if __name__=="__main__":
    app.run(debug=True)

