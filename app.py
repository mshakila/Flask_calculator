from flask import Flask, request, render_template, url_for

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
    else:
        result = num1 / num2
    
    return result



print(__name__)

if __name__ == "__main__":
    app.run(debug=True)

