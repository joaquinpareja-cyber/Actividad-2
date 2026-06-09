from flask import Flask, render_template_string, send_from_directory, request

app = Flask(__name__)

# Función para cargar el HTML
def cargar_html():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# Ruta principal
@app.route("/")
def index():
    return render_template_string(cargar_html())

# Rutas para servir CSS y JS
@app.route("/estilo.css")
def css():
    return send_from_directory(".", "estilo.css")

@app.route("/script.js")
def js():
    return send_from_directory(".", "script.js")

# Rutas simuladas para cada sección del menú
@app.route("/inicio")
def inicio():
    return "<h2>Bienvenido al Residencial El Expreso</h2><p>Comodidad y atención personalizada en Oruro.</p>"

@app.route("/habitaciones")
def habitaciones():
    return "<h2>Habitaciones</h2><p>Disponemos de habitaciones simples, dobles y familiares.</p>"

@app.route("/servicios")
def servicios():
    return "<h2>Servicios</h2><ul><li>Desayuno incluido</li><li>Recepción 24 horas</li><li>Estacionamiento privado</li></ul>"

@app.route("/contacto")
def contacto():
    return "<h2>Contacto</h2><p>Teléfono: +591 25234567 | Email: contacto@expreso.com</p>"

# Procesar formulario del Footer (Colaborador 2)
@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    mensaje = request.form.get("mensaje")
    return f"""
    <h2>Gracias {nombre}!</h2>
    <p>Hemos recibido tu mensaje: <em>{mensaje}</em></p>
    <p>Nos pondremos en contacto a través de {email}.</p>
    <a href="/">Volver al inicio</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
