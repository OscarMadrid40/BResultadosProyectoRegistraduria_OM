from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido

app=Flask(__name__)
cors = CORS(app)

miControladorResultado = ControladorResultado()
miControladorCandidato = ControladorCandidato()
miControladorMesa = ControladorMesa()
miControladorPartido = ControladorPartido()

"""
MESAS INICIO
"""
@app.route("/mesas",methods=['GET'])
def getMesas():
   json = miControladorMesa.index()
   return jsonify(json)

@app.route("/mesas",methods=['POST'])
def crearMesa():
   data = request.get_json()
   json = miControladorMesa.create(data)
   return jsonify(json)

@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
   json = miControladorMesa.show(id)
   return jsonify(json)

@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
   data = request.get_json()
   json = miControladorMesa.update(id, data)
   return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
   json = miControladorMesa.delete(id)
   return jsonify(json)

"""
CANDIDATOS 
"""
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
   json = miControladorCandidato.index()
   return jsonify(json)

@app.route("/candidatos",methods=['POST'])
def crearCandidato():
   data = request.get_json()
   json = miControladorCandidato.create(data)
   return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
   json = miControladorCandidato.show(id)
   return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
   data = request.get_json()
   json = miControladorCandidato.update(id, data)
   return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
   json = miControladorCandidato.delete(id)
   return jsonify(json)

"""
PARTIDOS
"""
@app.route("/partidos",methods=['GET'])
def getPartidos():
   json = miControladorPartido.index()
   return jsonify(json)

@app.route("/partidos",methods=['POST'])
def crearPartido():
   data = request.get_json()
   json = miControladorPartido.create(data)
   return jsonify(json)

@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
   json=miControladorPartido.show(id)
   return jsonify(json)

@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
   data = request.get_json()
   json = miControladorPartido.update(id,data)
   return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
   json=miControladorPartido.delete(id)
   return jsonify(json)

"""
RESULTADOS
"""
@app.route("/resultados", methods=['GET'])
def getResultados():
   json=miControladorResultado.index()
   return jsonify(json)

@app.route("/resultados/candidatos/<string:idCandidato>/mesas/<string:idMesa>",methods=['POST'])
def crearResultado(idCandidato, idMesa):
   data = request.get_json()
   json = miControladorResultado.create(data, idCandidato, idMesa)
   return jsonify(json)

@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
   json=miControladorResultado.show(id)
   return jsonify(json)

@app.route("/resultados/<string:idResultado>/candidatos/<string:idCandidato>/mesas/<string:idMesa>", methods=['PUT'])
def modificarResultado(idResultado, idCandidato, idMesa):
   data = request.get_json()
   json = miControladorResultado.update(idResultado,data,idCandidato,idMesa)
   return jsonify(json)

@app.route("/resultados/<string:idResultado>",methods=['DELETE'])
def eliminarResultado(idResultado):
   json=miControladorResultado.delete(idResultado)
   return jsonify(json)

@app.route("/resultados/mesas/<string:idMesa>",methods=['GET'])
def inscritosEnMesa(idMesa):
   json=miControladorResultado.listarInscritosEnMesa(idMesa)
   return jsonify(json)

@app.route("/resultados/partidos/<string:idPartido>",methods=['GET'])
def candidatosEnPartido(idPartido):
   json=miControladorResultado.listarCandidatosEnPartidos(idPartido)
   return jsonify(json)

"""
ASIGNACIONES
"""

@app.route("/candidatos/<string:id>/partidos/<string:idPartido>",methods=['PUT'])
def asignarPartidoACandidato(id,idPartido):
   json=miControladorCandidato.asignarPartido(id,idPartido)
   return jsonify(json)

@app.route("/mesas/<string:id>/candidatos/<string:idCandidato>",methods=['PUT'])
def asignarCandidatoAMesa(id,idCandidato):
   json=miControladorMesa.asignarCandidato(id,idCandidato)
   return jsonify(json)


@app.route("/",methods=['GET'])
def test():
   json = {}
   json["message"]="Server running..."
   return jsonify(json)

def loadFileConfig():
   with open('config.json') as f:
       data = json.load(f)
   return data

if __name__ == '__main__':
   dataConfig = loadFileConfig()
   print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
   serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
