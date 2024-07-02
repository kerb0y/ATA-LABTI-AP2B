from flask import Flask, render_template
 
app = Flask(__name__)

data = {
    "nama":"Ade Bintang Septian",
    "npm":"50423036",
    "kelas":"1IA21",
    "jurusan":"Informatika",
    "fakultas":"Teknologi Industri",
}

@app.route('/')
def index():
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run(port=8088)