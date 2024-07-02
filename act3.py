from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def index():
    return 'Web Ini Menggunakan Flask!'

@app.route('/data')
def data():
    return 'Nama saya Ade Bintang Septian dengan NPM 50423036'

if __name__ == "__main__":
    app.run(port=8088)
