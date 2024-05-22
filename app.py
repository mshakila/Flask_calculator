from flask import Flask, request, json, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask"

@app.route("/calculator", methods=["GET"])
def math_operator():
    operation=request.json["operation"]   # requesting from postman in form of json
    num1=request.json["num1"]
    num2=request.json["num2"]

    if operation=="add":
        result = (num1 + num2)
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = round(( num1 / num2),3)
    elif operation == "reminder":
        result = num1 % num2
    elif operation == "floor":
        result = num1 //num2
    else:
        return "check the operation given"
    
    #return jsonify(result)
    return "The operation is {} and the result is {}".format(operation,result)



print(__name__)

if __name__ == "__main__":
    app.run(debug=True)

