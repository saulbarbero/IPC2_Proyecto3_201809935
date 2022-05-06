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
    

    response = make_response(result, 200)
    response.mimetype = "text/plain"

    return response
    # return make_response(, 200)

@app.route("/prueba", methods=["GET"])
def getPrueba():
    return jsonify([{'nombre': 'usac', 'totalMensajes': 10,'positivos': 10, 'negativos': 20,'neutrales': 20}, {'nombre': 'calusac', 'totalMensajes': 1,'positivos': 100, 'negativos': 5,'neutrales': 28}])



@app.route("/xml", methods=["POST"])
def getXml():
    body=request.get_json()
    xml=body['xml']

    return jsonify({'xmlProcesado':processXml(xml)})


def processXml(xml):
    return xml


@app.route("/palabra", methods=["POST"])
def parseInfo():
    body=request.get_json()
    texto = body[texto]
    print(texto)
    response="la respuesta del proces"
    return {'data':response}