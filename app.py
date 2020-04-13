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
        return render_template('chatbot.html',msg="Hello, I am Anubha")
    else:
        return "<h1>Incorect Credentials</h1>"

@app.route('/userreply', methods=["POST","GET"])
def userreply():
    jobject = request.json
    msg=(jobject['msg'])
    return render_template('chatbot.html',msg=msg)
    

if __name__=="__main__":
    app.run(debug=True)

