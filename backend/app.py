from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

students = [
            [
                'Student_ID',
                'Student_Username',
                'Student_Password',
                'Email', 
                ['Enrolled_course1', 'Enrolled_course2']
            ]
           ]

app.route('/register', methods=['POST'])
def register():
    return

app.route('/login', methods=['POST'])
def login():
    return

app.route('/testimonials', methods=['GET'])
def returnRandomTestimonials():
    return

app.route('/enroll/<student_id>', methods=['POST'])
def enroll():
    return

app.route('/drop/<student_id>', methods=['DELETE'])
def drop():
    return

app.route('/courses', methods=['GET'])
def returnCourses():
    return

if __name__=='__main__':
    app.run()