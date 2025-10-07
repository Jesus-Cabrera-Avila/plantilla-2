from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")

@app.route('/animales_exoticos')
def animales():
    return render_template('animales.html')

@app.route('/carros_clasicos')
def carros():
    return render_template('carros.html')

@app.route('/maravillas_del_mundo')
def maravillas():
    return render_template('7_maravillas.htnl')

@app.route('/acerca_de')
def acerca():
    return render_template('acerca.html')

if __name__ == "__main__":
    app.run(debug=True)