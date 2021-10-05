from flask import Flask, jsonify

app = Flask(__name__)

from datos import datos_posicion

@app.route('/')
def Home():
    return jsonify(datos_posicion)

@app.route('/id/<string:id>')
def getProduct(id):
    name_found = [object_name for object_name in datos_posicion if object_name['norad'] == id.upper() or object_name['name'] == id.upper()]
    if (len(name_found) > 0):
        return jsonify(name_found)
    return jsonify({'message': 'Norad id Not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
