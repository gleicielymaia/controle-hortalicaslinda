from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Caminho do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "perdas.db")


# Conecta ao banco de dados
def conectar_banco():
    conexao = sqlite3.connect(DB_PATH)
    conexao.row_factory = sqlite3.Row
    return conexao


# Cria o banco e a tabela
def criar_banco():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS perdas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            data TEXT NOT NULL,
            motivo TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


# Página inicial e cadastro
@app.route("/", methods=["GET", "POST"])
def inicio():

    if request.method == "POST":

        produto = request.form["produto"]
        quantidade = request.form["quantidade"]
        data = request.form["data"]
        motivo = request.form["motivo"]

        conexao = conectar_banco()

        conexao.execute("""
            INSERT INTO perdas (produto, quantidade, data, motivo)
            VALUES (?, ?, ?, ?)
        """, (produto, quantidade, data, motivo))

        conexao.commit()
        conexao.close()

        return redirect("/perdas")

    return render_template("perdas.html")


# Lista as perdas
@app.route("/perdas")
def listar_perdas():

    conexao = conectar_banco()

    perdas = conexao.execute("""
        SELECT * FROM perdas
        ORDER BY id DESC
    """).fetchall()

    conexao.close()

    return render_template("perdas.html", perdas=perdas)


# Excluir perda
@app.route("/excluir/<int:id>")
def excluir_perda(id):

    conexao = conectar_banco()

    conexao.execute(
        "DELETE FROM perdas WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()

    return redirect("/perdas")


# Editar perda
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_perda(id):

    conexao = conectar_banco()

    if request.method == "POST":

        produto = request.form["produto"]
        quantidade = request.form["quantidade"]
        data = request.form["data"]
        motivo = request.form["motivo"]

        conexao.execute("""
            UPDATE perdas
            SET produto = ?,
                quantidade = ?,
                data = ?,
                motivo = ?
            WHERE id = ?
        """, (produto, quantidade, data, motivo, id))

        conexao.commit()
        conexao.close()

        return redirect("/perdas")

    perda = conexao.execute(
        "SELECT * FROM perdas WHERE id = ?",
        (id,)
    ).fetchone()

    conexao.close()

    if perda:
        return render_template("editar.html", perda=perda)

    return redirect("/perdas")


# Cria o banco ao iniciar
criar_banco()


if __name__ == "__main__":
    app.run(debug=True)