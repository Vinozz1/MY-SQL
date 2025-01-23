from flask import *
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/cendikia")
def cendikia():
    return render_template('cendikia.html')

@app.route('/CARI', methods = ["POST", "GET"])
def CARI(): 
    if request.method == "POST":
        key = request.form["keyword"]
        return redirect(f'https://scholar.google.co.id/scholar?hl=id&as_sdt=0%2C5&q={key}&btnG=')

if __name__ == '__main__':
    app.run(debug=True)