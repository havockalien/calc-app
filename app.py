from flask import Flask, request, jsonify
import calc  # your existing calculator module

app = Flask(__name__)

@app.route("/add", methods=["GET"])
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": calc.add(a, b)})

@app.route("/subtract", methods=["GET"])
def subtract():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": calc.subtract(a, b)})

@app.route("/multiply", methods=["GET"])
def multiply():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": calc.multiply(a, b)})

@app.route("/divide", methods=["GET"])
def divide():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    try:
        result = calc.divide(a, b)
        return jsonify({"result": result})
    except ZeroDivisionError:
        return jsonify({"error": "Division by zero"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
