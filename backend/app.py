from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import json, copy

app = Flask(__name__)
CORS(app)

students = [
            [
                'Student_ID',
                'Student_Username',
                'Student_Password',
                'Email', 
                [{'test_id': 1, "test_name": "Web", "test_inst": "Smith", "test_desc": "ipt", "test_dura": "8", "test_image": "images/fake.jpg"}] #enrolled courses
            ]
           ]

@app.route('/register', methods=['POST'])
def register():
    return

@app.route('/login', methods=['POST'])
def login():
    return

@app.route('/testimonials', methods=['GET'])
def returnRandomTestimonials():
    return

@app.route('/enroll/<student_id>', methods=['POST'])
def enroll(student_id):
    courseInfo = request.get_json()
    enrolled = False
    for i in range(len(students)):
        if students[i][0] == student_id:
            students[i][4].append(courseInfo)
            enrolled = True
    return enrolled

@app.route('/drop/<student_id>', methods=['DELETE'])
def drop(student_id):
    courseID = request.get_json()
    dropped = False
    for i in range(len(students)):
        if students[i][0] == student_id:
            for j in range(len(students[i][4])):
                if courseID == students[i][4][j]['id']:
                    students[i][4].pop(j)
                    dropped = True
    return dropped

@app.route('/courses', methods=['GET'])
def returnCourses():
    try:
        with open("courses.json", "r") as file:
            data = json.load(file)
        return json.dumps(data)
    except:
        return False

@app.route('/student_courses/<student_id>', methods=['GET'])
def returnStudentCourses(student_id):
    try:
        for i in range(len(students)):
            if students[i][0] == student_id:
                return json.dumps(students[i][4])
    except:
        return False

if __name__=='__main__':
    app.run()