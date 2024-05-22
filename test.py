from flask import Flask, request, json, jsonify

app = Flask(__name__)

@app.route("/cal", methods=["GET"])
def math_operation():
    operation = request.json["operation"]
    num1 = request.json["num1"]
    num2 = request.json["num2"]
    num3 = request.json["num3"]

    if operation == "add":
        result = num1 + num2 + num3
    elif operation == "multiply":
        result = num1 * num2 * num3
    else:
        return "check the operation"
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

