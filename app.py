from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/cadastrar-colheita", methods=["POST"])
def cadastrar_colheita():

    hortalica = request.form["hortalica"]
    quantidade = request.form["quantidade"]
    data = request.form["data"]

    print("Nova colheita cadastrada:")
    print("Hortaliça:", hortalica)
    print("Quantidade:", quantidade)
    print("Data:", data)

    return f"""
        <h1>Colheita cadastrada com sucesso!</h1>

        <p>Hortaliça: {hortalica}</p>
        <p>Quantidade: {quantidade}</p>
        <p>Data da colheita: {data}</p>

        <a href="/">Voltar para o cadastro</a>
    """


if __name__ == "__main__":
    app.run(debug=True) 
