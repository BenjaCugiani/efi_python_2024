from app import ma
from marshmallow import validates, ValidationError
from models import User, Equipo, Modelo, Categoria, Lista_Categoria

# Esquema para el modelo User
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password_hash = ma.auto_field()
    is_admin = ma.auto_field()

class UserMinimalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    username = ma.auto_field()

# Esquema para el modelo Categoria
class CategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categoria

    nombre = ma.auto_field()

# Esquema para el modelo Modelo
class ModeloSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Modelo

    nombre = ma.auto_field()
    fabricante_id = ma.auto_field()  # Incluye el ID del fabricante como campo (ajusta si tienes un esquema para fabricantes)

# Esquema para el modelo Equipo
class EquipoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Equipo

    id = ma.auto_field()
    nombre = ma.auto_field()
    modelo_id = ma.auto_field()
    categoria_id = ma.auto_field()
    costo = ma.auto_field()
    stock_id = ma.auto_field()
    modelo = ma.Nested(ModeloSchema)
    categoria = ma.Nested(CategoriaSchema)

    @validates('costo')
    def validate_costo(self, value):
        if value < 0:
            raise ValidationError("El costo no puede ser negativo")
        
# Esquema para el modelo Lista_Categoria
class Lista_CategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Lista_Categoria

    id = ma.auto_field()
    nombre = ma.auto_field()
    descripcion = ma.auto_field()
