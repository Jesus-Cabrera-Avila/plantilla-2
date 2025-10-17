from flask import Flask, render_template


app = Flask(__name__)

@app.route("/inicia secion")
def registro():
    return render_template("registro.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/animales")
def animalia():
    return render_template("animales.html")

@app.route("/Carros")
def carros():
    return render_template("carros.html")

@app.route("/maravillas")
def maravillas():
    return render_template("7_maravillas.html")

@app.route("/acerca_de")
def acerca():
    return render_template("acerca.html")

if __name__ == "__main__":
    app.run(debug=True)