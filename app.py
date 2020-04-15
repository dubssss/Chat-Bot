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
    if (msg== "Hi" or msg=="Hey" or msg=="Hello" or msg=="HELLO" or msg=="HI" or msg=="HEY"):
        return "hello"
    else:
        return "invalid"
    

if __name__=="__main__":
    app.run(debug=True)

