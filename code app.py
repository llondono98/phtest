from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/productos')
def productos():
    lista_productos = [
        {'nombre': 'Vitamina C', 'descripcion': 'Refuerza tu sistema inmune', 'precio': 15.99},
        {'nombre': 'Omega 3', 'descripcion': 'Cuida tu corazón', 'precio': 22.50},
        {'nombre': 'Magnesio', 'descripcion': 'Reduce el estrés', 'precio': 18.00},
    ]
    return render_template('productos.html', productos=lista_productos)


if __name__ == '__main__':
    app.run(debug=True)