from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)


def cargar_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/")
def index():
    return render_template_string(cargar_html())


@app.route("/estilo.css")
def css():
    return send_from_directory(".", "estilo.css")

@app.route("/script.js")
def js():
    return send_from_directory(".", "script.js")

if __name__ == "__main__":
    app.run(debug=True)
