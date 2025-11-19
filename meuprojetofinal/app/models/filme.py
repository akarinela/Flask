from app import db

class Filme(db.Model):
    __tablename__ = 'filme'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50))
    ano = db.Column(db.Integer)

    def __repr__(self):
        return self.titulo