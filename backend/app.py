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
                ['Enrolled_course1', 'Enrolled_course2']
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
    courseInfo = request.json()
    enrolled = False
    for i in range(len(students)):
        if students[i][0] == student_id:
            students[i][4].append(courseInfo)
            enrolled = True
    return enrolled

@app.route('/drop/<student_id>', methods=['DELETE'])
def drop(student_id):
    courseInfo = request.json()
    dropped = False
    for i in range(len(students)):
        if students[i][0] == student_id:
            for j in range(len(students[i][4])):
                if courseInfo == students[i][4][j]:
                    students[i][4].pop(j)
                    dropped = True
    return dropped

@app.route('/courses', methods=['GET'])
def returnCourses():
    with open("courses.json", "r") as file:
        data = json.load(file)
        courses = data['courses']
    return courses

@app.route('/student_courses/<student_id>', methods=['GET'])
def returnStudentCourses(student_id):
    for i in range(len(students)):
        if students[i][0] == student_id:
            courses = copy.deepcopy(students[i][4])
    return courses

if __name__=='__main__':
    app.run()