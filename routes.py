from app import app
from flask import render_template, request, redirect, url_for
from models import db, Equipo, Modelo, Categoria
from app import db
from flask import request, jsonify


# Rutas para el modelo Equipo

@app.route('/equipos')
def lista_equipos():
    equipos = Equipo.query.all()
    return render_template('equipos/lista_equipos.html', equipos=equipos)

@app.route('/equipos/nuevo', methods=['GET', 'POST'])
def nuevo_equipo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        modelo_id = request.form['modelo_id']
        categoria_id = request.form['categoria_id']
        costo = request.form['costo']
        stock_id = request.form['stock_id']
        nuevo_equipo = Equipo(nombre=nombre, modelo_id=modelo_id, categoria_id=categoria_id, costo=costo, stock_id=stock_id)
        db.session.add(nuevo_equipo)
        db.session.commit()
        return redirect(url_for('lista_equipos'))
    return render_template('equipos/nuevo_equipo.html')

@app.route('/equipos/<int:id>/editar', methods=['GET', 'POST'])
def editar_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    if request.method == 'POST':
        equipo.nombre = request.form['nombre']
        equipo.modelo_id = request.form['modelo_id']
        equipo.categoria_id = request.form['categoria_id']
        equipo.costo = request.form['costo']
        equipo.stock_id = request.form['stock_id']
        db.session.commit()
        return redirect(url_for('lista_equipos'))
    return render_template('equipos/editar_equipo.html', equipo=equipo)

@app.route('/equipos/<int:id>/eliminar', methods=['POST'])
def eliminar_equipo(id):
    equipo = Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return redirect(url_for('lista_equipos'))

# Rutas para el modelo Modelo

@app.route('/modelos')
def lista_modelos():
    modelos = Modelo.query.all()
    return render_template('modelos/lista_modelos.html', modelos=modelos)

@app.route('/modelos/nuevo', methods=['GET', 'POST'])
def nuevo_modelo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fabricante_id = request.form['fabricante_id']
        nuevo_modelo = Modelo(nombre=nombre, fabricante_id=fabricante_id)
        db.session.add(nuevo_modelo)
        db.session.commit()
        return redirect(url_for('lista_modelos'))
    return render_template('modelos/nuevo_modelo.html')

@app.route('/modelos/<int:id>/editar', methods=['GET', 'POST'])
def editar_modelo(id):
    modelo = Modelo.query.get_or_404(id)
    if request.method == 'POST':
        modelo.nombre = request.form['nombre']
        modelo.fabricante_id = request.form['fabricante_id']
        db.session.commit()
        return redirect(url_for('lista_modelos'))
    return render_template('modelos/editar_modelo.html', modelo=modelo)

@app.route('/modelos/<int:id>/eliminar', methods=['POST'])
def eliminar_modelo(id):
    modelo = Modelo.query.get_or_404(id)
    db.session.delete(modelo)
    db.session.commit()
    return redirect(url_for('lista_modelos'))

# Rutas para el modelo Categoria

@app.route('/categorias')
def lista_categorias():
    categorias = Categoria.query.all()
    return render_template('categorias/lista_categorias.html', categorias=categorias)

@app.route('/categorias/nuevo', methods=['GET', 'POST'])
def nueva_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nueva_categoria = Categoria(nombre=nombre)
        db.session.add(nueva_categoria)
        db.session.commit()
        return redirect(url_for('lista_categorias'))
    return render_template('categorias/nueva_categoria.html')

@app.route('/categorias/<int:id>/editar', methods=['GET', 'POST'])
def editar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    if request.method == 'POST':
        categoria.nombre = request.form['nombre']
        db.session.commit()
        return redirect(url_for('lista_categorias'))
    return render_template('categorias/editar_categoria.html', categoria=categoria)

@app.route('/categorias/<int:id>/eliminar', methods=['POST'])
def eliminar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return redirect(url_for('lista_categorias'))

@app.route('/')
def index():
    return render_template('index.html')

# Rutas para el modelo Lista_Categoria

@app.route('/lista_categorias')
def lista_lista_categorias():
    lista_categorias = lista_categorias.query.all()
    return render_template('lista_categorias/lista_lista_categorias.html', lista_categorias=lista_categorias)

@app.route('/lista_categorias/nuevo', methods=['GET', 'POST'])
def nueva_lista_categoria():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        nueva_lista_categoria = lista_categorias(nombre=nombre, descripcion=descripcion)
        db.session.add(nueva_lista_categoria)
        db.session.commit()
        return redirect(url_for('lista_lista_categorias'))
    return render_template('lista_categorias/nueva_lista_categoria.html')

@app.route('/lista_categorias/<int:id>/editar', methods=['GET', 'POST'])
def editar_lista_categoria(id):
    lista_categoria = lista_categorias.query.get_or_404(id)
    if request.method == 'POST':
        lista_categoria.nombre = request.form['nombre']
        lista_categoria.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('lista_lista_categorias'))
    return render_template('lista_categorias/editar_lista_categoria.html', lista_categoria=lista_categoria)

@app.route('/lista_categorias/<int:id>/eliminar', methods=['POST'])
def eliminar_lista_categoria(id):
    lista_categoria = lista_categorias.query.get_or_404(id)
    db.session.delete(lista_categoria)
    db.session.commit()
    return redirect(url_for('lista_lista_categorias'))
