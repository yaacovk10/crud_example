import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
students =[{"id":1,"name":"ohad"},{"id":2,"name":"dor"},{"id":3,  "name":"ana"}]

# CRUD

# Read - get all students
@app.route("/students",methods=["get"])
def get_students():
    return json.dumps(students)

# Create - add student
@app.route("/students",methods=["post"])
def add_student():
    data = request.json
    student = data['student']
    students.append({"name": student,"id":len( students)+1})
    return json.dumps(students)

# delete a student
@app.route("/students/<int:student_id>",methods=["delete"])
def del_students(student_id):
     # Find the index of the student with the given ID
    student_index = None
    for i, student in enumerate(students):
        if student["id"] == student_id:
            student_index = i
            break

    if student_index is not None:
        # Remove the student with the given ID from the list
        deleted_student = students.pop(student_index)
        return jsonify({"message": f"Deleted student with ID {student_id}", "deleted_student": deleted_student})
    else:
        return jsonify({"message": f"Student with ID {student_id} not found"}), 404


# Update a student
@app.route("/students/<int:student_id>",methods=["put"])
def upd_students(student_id):
    data = request.json

    # Find the index of the student with the given ID
    student_index = None
    for i, student in enumerate(students):
        if student["id"] == student_id:
            student_index = i
            break

    if student_index is not None:
        # Update the student's data with the provided data
        students[student_index].update(data)
        return jsonify({"message": f"Updated student with ID {student_id}", "updated_student": students[student_index]})
    else:
        return jsonify({"message": f"Student with ID {student_id} not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)