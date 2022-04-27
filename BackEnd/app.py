from flask import Flask, make_response, request, jsonify
from Recurso import Recurso
import xmltodict

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello World"


@app.route("/api/data",methods=['POST'])
def processingFile():
    content = xmltodict.parse(request.get_data())
    
    return make_response(content, 200)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=105)