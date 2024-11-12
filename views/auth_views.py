from datetime import timedelta
from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)
from app import db
from models import User
from schemas import UserSchema, UserMinimalSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    # Validar que la solicitud tenga Content-Type: application/json
    if not request.is_json:
        return jsonify({"Mensaje": "Tipo de contenido no soportado. Asegúrate de enviar JSON con Content-Type: application/json"}), 415

    data = request.get_json()

    # Validar que se hayan proporcionado las credenciales
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"Mensaje": "Credenciales no proporcionadas"}), 400

    username = data.get("username")
    password = data.get("password")

    usuario = User.query.filter_by(username=username).first()
    
    # Verificar las credenciales
    if usuario and check_password_hash(
        pwhash=usuario.password_hash, password=password
    ):
        access_token = create_access_token(
            identity=username,
            expires_delta=timedelta(minutes=20),
            additional_claims=dict(
                administrador=usuario.is_admin
            )
        )

        return jsonify({'Token': f'Bearer {access_token}'})

    # Mensaje en caso de credenciales incorrectas
    return jsonify({"Mensaje": "El usuario y la contraseña al parecer no coinciden"}), 401


@auth_bp.route('/users', methods=['GET', 'POST'])
@jwt_required()
def users():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if request.method == 'POST':
        if administrador is True:
            # Validar que la solicitud sea JSON
            if not request.is_json:
                return jsonify({"Mensaje": "Tipo de contenido no soportado. Asegúrate de enviar JSON con Content-Type: application/json"}), 415

            data = request.get_json()
            username = data.get('usuario')
            password = data.get('contrasenia')

            # Validar que se hayan proporcionado los campos necesarios
            if not username or not password:
                return jsonify({"Mensaje": "Nombre de usuario y contraseña son requeridos"}), 400

            try:
                nuevo_usuario = User(
                    username=username,
                    password_hash=generate_password_hash(password),
                    is_admin=False,
                )
                db.session.add(nuevo_usuario)
                db.session.commit()
                return jsonify(
                    {
                    "Mensaje": "Usuario creado correctamente",
                    "Usuario": nuevo_usuario.to_dict()
                    }
                )
            except:
                return jsonify({"Mensaje": "Falló la creación del nuevo usuario"}), 500
        else:
            return jsonify({"Mensaje": "Solo el admin puede crear nuevos usuarios"}), 403
    
    # Obtener todos los usuarios
    usuarios = User.query.all()
    if administrador is True:
        return UserSchema().dump(obj=usuarios, many=True)
    else:
        return UserMinimalSchema().dump(obj=usuarios, many=True)

# Ruta para actualizar un usuario específico (PUT)
@auth_bp.route("/users/<int:id>", methods=["PUT"])
@jwt_required()
def update_user(id):
    additional_data = get_jwt()
    administrador = additional_data.get("administrador", False)

    if administrador:
        data = request.get_json()
        usuario = User.query.get_or_404(id)

        # Actualiza los campos del usuario
        if "usuario" in data:
            usuario.username = data.get("usuario")
        if "contrasenia" in data:
            new_password = data.get("contrasenia")
            usuario.password_hash = generate_password_hash(new_password, method="pbkdf2", salt_length=8)
        if "is_admin" in data:
            usuario.is_admin = data.get("is_admin", False)

        try:
            db.session.commit()
            return jsonify({"Mensaje": "Usuario actualizado correctamente."}), 200
        except:
            db.session.rollback()
            return jsonify({"Error": "Ocurrió un error al actualizar el usuario."}), 500

    return jsonify({"Mensaje": "Usted no está habilitado para actualizar un usuario."}), 403

# Ruta para eliminar un usuario específico (DELETE)
@auth_bp.route("/users/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_user(id):
    additional_data = get_jwt()
    administrador = additional_data.get("administrador", False)

    if administrador:
        usuario = User.query.get_or_404(id)
        try:
            db.session.delete(usuario)
            db.session.commit()
            return jsonify({"Mensaje": "Usuario eliminado correctamente."}), 200
        except:
            return jsonify({"Error": "Ocurrió un error al eliminar el usuario."}), 500

    return jsonify({"Mensaje": "Usted no está habilitado para eliminar un usuario."}), 403


