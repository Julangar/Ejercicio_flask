from flask import Flask, render_template
app = Flask(__name__)

@app.route("/Julian")
def Inicio():
   return render_template("Hoja_de_vida/Inicio.html")

@app.route("/Julio")
def Presentacion():
   return render_template("html-main/Presentacion.html")

@app.route("/Miguel")
def Index():
   return render_template("TrabajosPrograAvanzada-main/Index.html")

if __name__ == '__main__':
   app.run(debug = True)