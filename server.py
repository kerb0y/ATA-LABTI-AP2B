
from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route("/get_students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/add_student", methods=["POST"])
def add_student():
    new_student = request.json
    for student in students:
        if student["npm"] == new_student["npm"]:
            return jsonify({"status": "error", "message": "NPM sudah ada"}), 400
    students.append(new_student)
    return jsonify({"status": "success", "students": students})

@app.route("/delete_student", methods=["DELETE"])
def delete_student():
    npm_to_delete = request.args.get("npm")
    global students
    students = [student for student in students if student["npm"] != npm_to_delete]
    return jsonify({"status": "success", "students": students})

if __name__ == "__main__":
    app.run(debug=True, port=5000)