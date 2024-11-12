from app import db

# Modelo de equipo
class Equipo(db.Model):
    __tablename__ = 'equipos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelos.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    costo = db.Column(db.Integer, nullable=False)
    stock_id = db.Column(db.Integer, nullable=False)

    # Relación con el modelo y la categoría
    modelo = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))
    categoria = db.relationship('Categoria', backref=db.backref('equipos', lazy=True))

    def __repr__(self):
        return f'<Equipo {self.nombre}>'

# Modelo de modelo (del equipo)
class Modelo(db.Model):
    __tablename__ = 'modelos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fabricante_id = db.Column(db.Integer, nullable=False)  # Se puede reemplazar con una ForeignKey si hay un modelo de fabricantes

    def __repr__(self):
        return f'<Modelo {self.nombre}>'

# Modelo de categoría
class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Categoria {self.nombre}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    is_admin = db.Column(db.Boolean)


    def to_dict(self):
        return dict(
            username=self.username,
            password=self.password_hash
        )

class Lista_Categoria(db.Model):
    __tablename__ = 'lista_categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Lista_Categoria {self.nombre}>"
