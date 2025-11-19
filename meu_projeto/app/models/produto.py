from app import db

class Produto(db.Model):

    __tablename__ = 'produto'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False) 
    preco = db.Column(db.Float)                     
    quantidade = db.Column(db.Integer)             

    def __repr__(self):
        return self.nome