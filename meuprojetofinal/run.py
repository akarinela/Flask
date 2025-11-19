from app import app, db                 
from app.models.filme import Filme    # <-- Importa o modelo Filme
from app.controllers import views     # <-- Importa as rotas

def criar_tabelas():
    print("Criando tabelas...")
    with app.app_context():
        db.create_all()
    print("Tabelas prontas.")

if __name__ == '__main__':
    criar_tabelas()
    app.run(debug=True, port=5000)