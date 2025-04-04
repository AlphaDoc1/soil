from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_moisture = {"moisture_percent": None}

@app.route("/api/moisture", methods=["POST"])
def receive_moisture():
    global latest_moisture
    data = request.get_json()
    print("Received Data:", data)
    if data and "moisture_percent" in data:
        latest_moisture["moisture_percent"] = data["moisture_percent"]
        return jsonify({"message": "Moisture data received!"}), 200
    return jsonify({"error": "Invalid data"}), 400

@app.route("/api/moisture", methods=["GET"])
def get_moisture():
    return jsonify(latest_moisture)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
