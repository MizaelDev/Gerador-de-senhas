from flask import Flask, jsonify, request
from hibp import check_password
from password_gen import generate_password, calculate_entropy

app = Flask(__name__)

@app.route("/api/generate")
def generate():
    length = int(request.args.get("length", 16))
    length = max(8, min(64, length))  # limita entre 8 e 64
    password = generate_password(length)
    return jsonify({
        "password": password,
        "entropy": round(calculate_entropy(password), 1)
    })

@app.route("/api/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")

    if not password:
        return jsonify({"error": "Senha não informada"}), 400

    count = check_password(password)
    return jsonify({
        "pwned": count > 0,
        "count": count,
        "entropy": round(calculate_entropy(password), 1)
    })

if __name__ == "__main__":
    app.run(debug=True)