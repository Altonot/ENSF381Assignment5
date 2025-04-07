from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

students = [['Student_ID', 'Student_Username', 'Student_Password', 'Email', ['Enrolled_course1', 'Enrolled_course2']]]

app.route('/test', methods=['POST'])
def test():
    return

if __name__=='__main__':
    app.run()