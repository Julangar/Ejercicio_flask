from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def Menu():
   return render_template("Menu.html")

@app.route("/Julian")
def Inicio():
   return render_template("HojaDeVida/Inicio.html")

@app.route("/DatosJulian")
def DBasicos():
   return render_template("HojaDeVida/DatosBasicos.html")

@app.route("/FormacionJulian")
def Formacion():
   return render_template("HojaDeVida/FormacionAcademica.html")

@app.route("/TecnologiasJulian")
def Tecnologias():
   return render_template("HojaDeVida/TecnologiasDeInteres.html")

@app.route("/Julio")
def Presentacion():
   return render_template("html-main/Presentacion.html")

@app.route("/DatosJulio")
def Datos():
   return render_template("html-main/Datos.html")

@app.route("/InfoJulio")
def Informacion():
   return render_template("html-main/Informacion.html")

@app.route("/TecnologiasJulio")
def Tecno():
   return render_template("html-main/Tecnologias.html")

@app.route("/Miguel")
def Index():
   return render_template("TrabajosPrograAvanzada-main/Index.html")

@app.route("/pg2Miguel")
def Pg2():
   return render_template("TrabajosPrograAvanzada-main/pg2.html")

@app.route("/pg3Miguel")
def Pg3():
   return render_template("TrabajosPrograAvanzada-main/pg3.html")

@app.route("/pg4Miguel")
def Pg4():
   return render_template("TrabajosPrograAvanzada-main/pg4.html")

if __name__ == '__main__':
   app.run(debug = True)