#!/usr/bin/python3
"""remmber the shebang"""
from flask import Flask, request

app = Flask(__name__)

@app.route("/result",methods=["POST","GET"])
def result():
    """example"""
    output = request.get_json()
    if len(output.keys()) < 2:
        return {"Status":"BAD Response"}
    return {"API";"Response Positive"}


if __name__ == '__main__':
    app.run(debug=True, port=5000)

