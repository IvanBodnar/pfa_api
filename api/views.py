from app import app
from flask import jsonify
from api.consultas import Consultas
from api.models import Hechos

# PRUEBA FABRICCCC

consultas = Consultas(Hechos())


@app.route('/siniestros/api/search/', methods=['GET'])
def search():
    return jsonify(consultas.consulta_prueba())


@app.route('/siniestros/api/search/<mes>/', methods=['GET'])
def search_mes(mes):
    return jsonify(consultas.consulta_mes(mes.upper()))


@app.route('/siniestros/api/search/espacial/', methods=['GET'])
def search_espacial():
    return jsonify(consultas.consulta_espacial())
