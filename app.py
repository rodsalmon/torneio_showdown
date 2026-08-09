from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pagina1")
def pagina1():
    return render_template("pagina1.html")


@app.route("/pagina2/subpagina1")
def subpagina1():
    return render_template("subpagina1.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
