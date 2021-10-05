from flask import Flask,render_template, request
import test

app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])
def page():
    test.generar()
    return render_template("home.html")

@app.route("/buscar",methods = ['GET'])
def procesar():
    pr = request.args.get('id')
    test.filtrar(pr)
    return render_template("redireccionar.html")

@app.route("/ver")
def search():
    return render_template("homeb.html")

@app.route("/ocultar")
def ocult():
    return render_template("oculto.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True, port=4000)
