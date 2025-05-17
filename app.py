from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🔁 Reemplaza esta URL con tu Webhook real de Make
MAKE_WEBHOOK_URL = "https://hook.us2.make.com/h4il23g008txq2dri4keaewfp3oeaxst"

@app.route('/evaluacion', methods=['POST'])
def recibir_evaluacion():
    data = request.json
    try:
        r = requests.post(MAKE_WEBHOOK_URL, json=data)
        if r.status_code == 200:
            return jsonify({"message": "Evaluación enviada a Make"}), 200
        else:
            return jsonify({"error": "Error enviando a Make", "status_code": r.status_code}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
