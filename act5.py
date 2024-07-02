from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
students = [
    {
        "nama": "John Cahyono",
        "npm": "50347723",
        "kelas": "3IA23",
    },
    {
        "nama": "Arip Cahyono",
        "npm": "50347722",
        "kelas": "3IA23",
    },
    {
        "nama": "Asep Wahyudi",
        "npm": "51464361",
        "kelas": "2IA21",
    },
]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/mahasiswa/<string:npm>", methods=["GET"])
def get_mahasiswa_by_npm(npm):
    for mahasiswa in students:
        if mahasiswa["npm"] == npm:
            return jsonify(mahasiswa)
    return jsonify({"error": "Mahasiswa tidak ditemukan"}), 404

@app.route("/mahasiswa", methods=["GET", "POST"])
def add_or_create_mahasiswa():
    if request.method == "GET":
        return jsonify(students)

    new_mahasiswa = {
        "nama": request.form.get("nama"),
        "npm": request.form.get("npm"),
        "kelas": request.form.get("kelas"),
    }

    if not new_mahasiswa["nama"] or not new_mahasiswa["npm"]:
        return jsonify({"error": "Data mahasiswa tidak valid!"}), 400

    for mahasiswa in students:
        if mahasiswa["npm"] == new_mahasiswa["npm"]:
            return (
                jsonify(
                    {"error": f"Mahasiswa dengan NPM {new_mahasiswa['npm']} sudah ada"}
                ),
                409,
            )

    students.append(new_mahasiswa)
    return (
        jsonify({"message": "Mahasiswa berhasil ditambah", "data": new_mahasiswa}),
        201,
    )

@app.route("/mahasiswa/<string:npm>", methods=["PUT"])
def update_mahasiswa_by_npm(npm):
    updated_data = {
        "nama": request.form.get("nama"),
        "kelas": request.form.get("kelas"),
    }

    if not updated_data["nama"] and not updated_data["kelas"]:
        return jsonify({"error": "Data mahasiswa tidak valid!"}), 400

    for i, mahasiswa in enumerate(students):
        if mahasiswa["npm"] == npm:
            students[i].update({k: v for k, v in updated_data.items() if v})
            return jsonify(
                {"message": "Data mahasiswa berhasil diubah", "data": students[i]}
            )
    return jsonify({"error": "Mahasiswa tidak ditemukan"}), 404

@app.route("/mahasiswa/<string:npm>", methods=["DELETE"])
def delete_mahasiswa_by_npm(npm):
    for i, mahasiswa in enumerate(students):
        if mahasiswa["npm"] == npm:
            del students[i]
            return jsonify({"message": "Mahasiswa berhasil dihapus"})
    return jsonify({"error": "Mahasiswa tidak ditemukan"}), 404

if __name__ == "__main__":
    app.run(debug=True)