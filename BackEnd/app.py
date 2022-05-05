from flask import Flask, make_response, request, jsonify
from controller.Recurso import Recurso
from edd.lista import lista
from controller.mensajeController import MensajeController
import xmltodict
import json

app = Flask(__name__)


@app.route("/api/data",methods=['POST'])
def processingFile():
    test = request.get_data()
    content = xmltodict.parse(request.get_data())
    controller = MensajeController(test)
    result = controller.analizarEntrada()

    if result == "Error":
        return make_response(f'{"Error": "Se encontro un error en el analisis"}', 500)
    

    return jsonify(json.loads(result))
    # return make_response(, 200)


@app.route("/prueba", methods=["GET"])
def getPrueba():
    return jsonify([{'nombre': 'usac', 'positivos': 10, 'negativos': 20}, {'nombre': 'calusac', 'positivos': 5, 'negativos': 4}])
