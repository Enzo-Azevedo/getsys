from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receber_dados():
    dados = request.json  # ou request.form se for form-data
    return jsonify({"recebido": dados}), 200