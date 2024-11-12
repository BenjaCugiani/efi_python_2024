from flask import Blueprint, request, make_response, jsonify
from app import db
from models import Equipo, Modelo, Categoria
from schemas import CategoriaSchema, ModeloSchema, EquipoSchema

equipo_bp = Blueprint('equipos', __name__)

@equipo_bp.route('/categorias', methods=['GET'])
def categorias():
    categorias = Categoria.query.all()
    return CategoriaSchema().dump(categorias, many=True)

@equipo_bp.route('/modelos', methods=['GET', 'POST'])
def modelos():
    if request.method == 'POST':
        data = request.get_json()
        errors = ModeloSchema().validate(data)
        if errors:
            return make_response(jsonify(errors), 400)

        nuevo_modelo = Modelo(
            nombre=data.get('nombre'),
            categoria_id=data.get('categoria_id'),
            costo=data.get('costo'),
            stock_id=data.get('stock_id')
        )
        db.session.add(nuevo_modelo)
        db.session.commit()
        return ModeloSchema().dump(nuevo_modelo), 201

    modelos = Modelo.query.all()
    return ModeloSchema().dump(modelos, many=True)

@equipo_bp.route('/equipos', methods=['GET', 'POST'])
def equipos():
    if request.method == 'POST':
        data = request.get_json()
        errors = EquipoSchema().validate(data)
        if errors:
            return make_response(jsonify(errors), 400)
        
        nuevo_equipo = Equipo(
            nombre=data.get('nombre'),
            modelo_id=data.get('modelo_id'),
            categoria_id=data.get('categoria_id'),
            costo=data.get('costo'),
            stock_id=data.get('stock_id')
        )
        db.session.add(nuevo_equipo)
        db.session.commit()
        return EquipoSchema().dump(nuevo_equipo), 201

    equipos = Equipo.query.all()
    return EquipoSchema().dump(equipos, many=True)
