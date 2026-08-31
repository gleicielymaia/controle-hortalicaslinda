from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("perdas.html")


@app.route("/perdas")
def perdas():
    return render_template("perdas.html")


if __name__ == "__main__":
    app.run(debug=True)