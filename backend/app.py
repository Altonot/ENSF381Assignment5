from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

app.route('/test', methods=['POST'])
def test():
    return

if __name__=='__main__':
    app.run()