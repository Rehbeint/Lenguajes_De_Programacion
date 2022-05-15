 # Integrantes: Javier Rehbein; Cristobal Galindo;
 # Asignatura: Lenguajes de Programacion;
 # Profesor: Cristhian Aguilera;
 # Trabajo: Assigment 07


from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def pagina_web():
    return render_template("Assigment.html")

if __name__ == "__main__":
    app.run(debug=True)
