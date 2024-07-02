from flask import Flask, request, render_template

app = Flask(__name__)

accounts = {}

def create_account(username, psasword):
    if get_account(username):
        return False
    
    accounts[username] = {"username": username, "password": psasword}
    return True

def get_account(username):
    return accounts.get(username)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if get_account(username) == None:
            return "Username tidak ditemukan"
        if accounts[username]["password"] == password:
            return f"Selamat datang, {username}!"
        else:
            return "Password Salah!"
    return "Halaman Login"
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not create_account(username, password):
            return "Username sudah digunakan!"
        return accounts
    return "Halaman register"       
   
if __name__ == "__main__":
    app.run(debug=True)