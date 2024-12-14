from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/test")
def test():
    return "Test is working"