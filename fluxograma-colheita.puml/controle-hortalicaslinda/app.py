from flask import Flask, render_template, request

app = Flask(__name__)

# Lista para armazenar as colheitas cadastradas
colheitas = []


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastrar-colheita", methods=["POST"])
def cadastrar_colheita():

    hortalica = request.form["hortalica"]
    quantidade = request.form["quantidade"]
    data = request.form["data"]

    # Adiciona a colheita à lista
    colheitas.append({
        "hortalica": hortalica,
        "quantidade": quantidade,
        "data": data
    })

    print("Nova colheita cadastrada:")
    print("Hortaliça:", hortalica)
    print("Quantidade:", quantidade)
    print("Data:", data)

    return render_template(
        "colheitas.html",
        colheitas=colheitas
    )


if __name__ == "__main__":
    app.run(debug=True)