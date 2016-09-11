from flask import Flask,request,url_for,redirect,render_template, flash, session
import json, urllib2

app=Flask(__name__)

app.config['SECRET_KEY'] = "secret key"
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/", methods = ["POST", "GET"])
def index():
    return render_template ("index.html")

if __name__ == '__main__':
    app.debug = False
    app.run(host = '0.0.0.0', port=8023)