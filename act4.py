from flask import Flask
# from werkzeug.routing import Mao, rules

app = Flask(__name__)

students = [
    {
        "nama": "Ade Bintang Septian",
        "npm": "50423036",
        "kelas": "1IA21",
    },
    {
        "nama": "Arip",
        "npm": "501284198",
        "kelas": "1IA22",
    },
    {
        "nama": "Cahyono",
        "npm": "519842916",
        "kelas": "1IA22",
    },
]

@app.route("/data/<val>")
def data(val):
    matching_items = []
    for item in students:
        for value in item.values():
            if isinstance(value, str) and val.lower() in value.lower():
                matching_items.append(item)
                break
    if matching_items:
        return {"data": matching_items}
    else:
        return {"data tidak ditemukan"}
    
if __name__ == "__main__":
    app.run(debug=True)
        