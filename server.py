from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///School.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Student(db.Model):
    tablename = "student"
    student_id = db.Column(db.String(50), primary_key=True)
    student_firstname = db.Column(db.String(50))
    student_midname = db.Column(db.String(50))
    student_lname = db.Column(db.String(50))

    def __init__(self, student_id, student_firstname, student_midname, student_lname):
        self.student_id = student_id
        self.student_firstname = student_firstname
        self.student_midname = student_midname
        self.student_lname = student_lname

class StudentSchema(ma.Schema):
    class Meta:
        fields = ("student_id", "student_firstname", "student_midname", "student_lname")

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@app.route('/students', methods=['POST'])
def create_student():
    student_id = request.json.get('student_id')
    student_firstname = request.json.get('student_firstname')
    student_midname = request.json.get('student_midname')
    student_lname = request.json.get('student_lname')
    new_student = Student(student_id, student_firstname, student_midname, student_lname)
    db.session.add(new_student)
    db.session.commit()

    return student_schema.jsonify(new_student)

@app.route('/students', methods=['GET'])
def read_all():
    students = Student.query.all()
    result = students_schema.dump(students)
    return students_schema.jsonify(result).data

@app.route('/students/<student_id>', methods=['GET'])
def read_student(student_id):
    student = Student.query.get(student_id)
    result = student_schema.dump(student)
    return student_schema.jsonify(result)

@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    student_firstname = request.json.get('student_firstname')
    student_lname = request.json.get('student_lname')
    student_midname = request.json.get('student_midname')
    student.student_firstname = student_firstname
    student.student_lname = student_lname
    student.student_midname = student_midname
    db.session.commit()
    return student_schema.jsonify(student)

@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    db.session.delete(student)
    db.session.commit()
    return student_schema.jsonify(student)

if __name__ == '__main__':
    app.run(debug=True) 