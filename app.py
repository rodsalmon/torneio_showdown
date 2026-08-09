from flask import Flask, render_template, request, redirect, url_for, Response
from functools import wraps
import os

app = Flask(__name__)

# --- Autenticação simples (usuário e senha) ---
# Em produção, defina APP_USER e APP_PASS como variáveis de ambiente
# na plataforma de deploy (nunca deixe senha fixa no código real).
USERNAME = os.environ.get("APP_USER", "admin")
PASSWORD = os.environ.get("APP_PASS", "admin")


def check_auth(username, password):
    return username == USERNAME and password == PASSWORD


def authenticate():
    return Response(
        "Acesso restrito. Informe usuário e senha.",
        401,
        {"WWW-Authenticate": 'Basic realm="Login necessário"'},
    )


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


# --- "Banco de dados" em memória (zera quando o app reinicia) ---
registros = []


@app.route("/", methods=["GET", "POST"])
@requires_auth
def index():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        mensagem = request.form.get("mensagem", "").strip()
        if nome and mensagem:
            registros.append({"nome": nome, "mensagem": mensagem})
        return redirect(url_for("index"))
    return render_template("index.html", registros=registros)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
