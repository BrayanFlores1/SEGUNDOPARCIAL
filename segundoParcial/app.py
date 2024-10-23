from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# INGE ESTA ES COMO MI BASE DE DATOS FICTICIA
productos = [
    {'id': 1, 'nombre': 'tenis', 'cantidad': 10, 'precio': 500, 'fecha_vencimiento': '2024-12-01', 'categoria': 'Categoría A'},
    {'id': 2, 'nombre': 'chamarras', 'cantidad': 20, 'precio': 300, 'fecha_vencimiento': '2024-11-15', 'categoria': 'Categoría B'},
    {'id': 3, 'nombre': 'pantalones', 'cantidad': 20, 'precio': 300, 'fecha_vencimiento': '2024-11-15', 'categoria': 'Categoría B'},
    {'id': 4, 'nombre': 'zapatos', 'cantidad': 20, 'precio': 300, 'fecha_vencimiento': '2024-11-15', 'categoria': 'Categoría B'},
]

@app.route('/')
def home():
    return render_template('productos.html', productos=productos)

@app.route('/nuevo-producto', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        nuevo_id = len(productos) + 1
        nuevo_producto = {
            'id': nuevo_id,
            'nombre': request.form['descripcion'],
            'cantidad': request.form['cantidad'],
            'precio': request.form['precio'],
            'fecha_vencimiento': request.form['fecha_vencimiento'],
            'categoria': request.form['categoria']
        }
        productos.append(nuevo_producto)
        return redirect(url_for('nuevo_producto'))  # Redirige a la misma página para mostrar el nuevo producto

    return render_template('nuevoproducto.html', productos=productos)

@app.route('/editar/<int:producto_id>', methods=['GET', 'POST'])
def editar(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if request.method == 'POST':
        producto['nombre'] = request.form['descripcion']
        producto['cantidad'] = request.form['cantidad']
        producto['precio'] = request.form['precio']
        producto['fecha_vencimiento'] = request.form['fecha_vencimiento']
        producto['categoria'] = request.form['categoria']
        return redirect(url_for('home'))

    return render_template('nuevoproducto.html', producto=producto)

@app.route('/eliminar/<int:producto_id>', methods=['POST'])
def eliminar(producto_id):
    global productos
    productos = [p for p in productos if p['id'] != producto_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
