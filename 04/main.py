from flask import *
import secrets
from datetime import timedelta

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.permanent_session_lifetime = timedelta(minutes=5)
# session.permanent = True

users = [
    {
        "username": "admin",
        "password": '123456',
        "role": 'admin'
    },
    {
        "username": "sma.23.2024",
        "password": '090109',
        "role": 'admin'
    },
    {
        "username": "jasen",
        "password": 'j',
        "role": 'admin'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    if session.get("user") and session.get("role") == "admin":
        return render_template("admin.html")
    else:
        return redirect(url_for("login"))
    
# @app.route('/creator')
# def creator():
    # if session.get("user") and session.get("role") == "creator":
    #     return render_template("creator.html")
    # else:
    #     return redirect(url_for("login"))

# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]
        
#         # for user in users:
#         #     if username == user["username"] and password == user["password"]:
#         #         session["user"] = username
#         #         session["role"] = user["role"]
                
#         #         if user["role"] == "admin":
#         #             return redirect(url_for("admin"))
#         #         elif user["role"] == "creator":
#         #             return redirect(url_for("creator"))
#         #         else:
#         #             return redirect(url_for("home"))
        
#         # return redirect(url_for("login"))
#         for i in users:
#             if (username == i["username"]) and (password == i["password"]):
#                 session["user"] = username
#                 # session["role"] = i["role"]
#                 # if i["role"] == "admin":
#                 #     return redirect(url_for("admin"))
#                 # elif i["role"] == "creator":
#                 #     return redirect(url_for("creator"))
#                 # else:
#                 #     return redirect(url_for("home"))
#                 return redirect(url_for(i["role"]))
#             else:
#                 return redirect(url_for("login"))
#     else:
#         return render_template('login.html')
    
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        for i in users:
            if username == i["username"] and password == i["password"]:
                session["user"] = username
                session["role"] = i["role"]
                # return redirect(url_for(i["role"])) 
                return redirect(url_for("admin")) 
        else:
            return redirect(url_for("login"))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("role", None)
    # all session:
    # session.clear()
    return redirect(url_for("login"))

@app.route("/bio", methods=["POST", "GET"])
def bio():
    return render_template('bio.html',
                         nama=request.form["nama"],
                         kelas=request.form["kelas"],
                         email=request.form["email"],
                         tempat=request.form["tempat"],
                         tanggal=request.form["tanggal"],
                         cita=request.form["cita"],
                         agama=request.form["agama"],
                         tentang=request.form["Tentang"],
                         )

if __name__ == '__main__':
    app.run(debug=True)