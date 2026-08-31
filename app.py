from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista para armazenar as perdas
perdas = []


@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":

        produto = request.form["produto"]
        quantidade = request.form["quantidade"]
        data = request.form["data"]
        motivo = request.form["motivo"]

        perda = {
            "produto": produto,
            "quantidade": quantidade,
            "data": data,
            "motivo": motivo
        }

        perdas.append(perda)

        return redirect("/perdas")

    return render_template("perdas.html")


@app.route("/perdas")
def listar_perdas():
    return render_template("perdas.html", perdas=perdas)


if __name__ == "__main__":
    app.run(debug=True)