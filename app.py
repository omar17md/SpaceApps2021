from flask import Flask,render_template
import test

app = Flask(__name__)

test.generar()

@app.route("/",methods = ['GET','POST'])
def page():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True, port=4000)