from flask import *

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/bio', methods = ["POST", "GET"])
def bio():
    return render_template("bio.html",
                           nama = request.form["nama"],
                           kelas = request.form["kelas"],
                           email = request.form["email"],
                           tempat = request.form["tempat"],
                           tgl = request.form["tgl"],
                           cita = request.form["cita"],
                           agama = request.form["agama"],
                           tentang = request.form["tentang"],
                           )
if __name__ == '__main__':
    app.run(debug=True)