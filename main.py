from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal (Menu con 2 botones)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta Ejercicio 1: Calculo de compras de tarros de pintura
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        # Calculo de descuento segun edad
        if 18 <= edad <= 30:
            porcentaje_descuento = 0.15
        elif edad > 30:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.0

        descuento = total_sin_descuento * porcentaje_descuento
        total_pagar = total_sin_descuento - descuento

        return render_template(
            'ejercicio1.html',
            resultado=True,
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total_pagar=total_pagar
        )

    return render_template('ejercicio1.html', resultado=False)

# Ruta Ejercicio 2: Inicio de sesion
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario == 'juan' and contrasena == 'admin':
            mensaje = f"Bienvenido Administrador {usuario}"
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = f"Bienvenido Usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)