from flask import Flask,render_template

app = Flask(__name__)


@app.route("/",methods = ['GET','POST'])
def page():
    return render_template("home.html")

app.run(port=8000)