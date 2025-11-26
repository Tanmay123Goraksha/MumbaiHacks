from flask import Flask, request, jsonify
from ai_agent import dream_to_financial_plan

app = Flask(__name__)

@app.route("/dream", methods=["POST"])
def handle_dream():
    data = request.json

    if not data or "dream" not in data:
        return jsonify({"error": "Please send { 'dream': 'your goal' }"}), 400

    dream = data["dream"]
    result = dream_to_financial_plan(dream)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
