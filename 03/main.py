from flask import *
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    name = request.args.get("name")
    umur = int(request.args.get("umur"))
    return render_template("home.html", name = name, umur=umur)

@app.route('/calculator')
def calculator():
    n1 = float(request.args.get('n1'))
    n2 = float(request.args.get('n2'))
    op = request.args.get('op', default='add')

    if op == 'add':
        result = n1 + n2
        symbol = '+'
    elif op == 'multiply':
        result = n1 * n2
        symbol = '*'
    elif op == 'minus':
        result = n1 - n2
        symbol = '-'
    elif op == 'divide':
        result = n1 // n2
        symbol = '//'
    elif op == 'modulus':
        result = n1 % n2
        symbol = '%'
    elif op == 'pangkat':
        result = n1 ** n2
        symbol = '**'

    return render_template( 'calculator.html',n1=n1,n2=n2,operator=symbol,result=result)

if __name__ == "__main__":
    app.run(debug=True)