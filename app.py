from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("//registro", methods=["GET", "POST"])
def registro():
    error = None  

    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        dia = request.form.get("dia")
        mes = request.form.get("mes")
        año = request.form.get("año")
        genero = request.form.get("genero")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if password != confirm_password:
            error = "Las contraseñas no coinciden."
        elif not nombre or not apellido or not email or not password or not confirm_password:
            error = "Todos los campos son obligatorios."

        if not error:
            return redirect(url_for("index"))

    return render_template("registro.html", error=error)



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
