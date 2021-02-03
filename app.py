from flask import Flask, jsonify
from flask_cors import CORS

from ScrapForNews import getNDTVNewsHeadLines
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/getNews')
def getNews():
    data = getNDTVNewsHeadLines()
    json_output = {
        "status":200,
        "data":data
    }
    return jsonify(json_output)


if __name__ == '__main__':
    app.run()
