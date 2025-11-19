from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.filme import Filme 

# Rota principal: Redireciona direto para /filmes
@app.route('/')
def index():
    return redirect(url_for('listar_filmes'))

# Lista os filmes
@app.route('/filmes')
def listar_filmes():
    todos_filmes = Filme.query.all()
    return render_template('filmes.html', filmes=todos_filmes)

# Adiciona filme
@app.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form.get('titulo')
    genero = request.form.get('genero')
    ano_str = request.form.get('ano')
    
    # Converte ano para int se existir
    ano = int(ano_str) if ano_str else None

    if titulo:
        # Cria o novo Filme
        novo_filme = Filme(titulo=titulo, genero=genero, ano=ano)
        db.session.add(novo_filme)
        db.session.commit()

    return redirect(url_for('listar_filmes'))

# Exclui filme
@app.route('/excluir/<int:id>')
def excluir(id):
    filme = Filme.query.get(id)

    db.session.delete(filme)
    db.session.commit()

    return redirect(url_for('listar_filmes'))

# Edita filme
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    filme = Filme.query.get(id)

    if request.method == 'POST':
        filme.titulo = request.form.get('titulo')
        filme.genero = request.form.get('genero')
        ano_str = request.form.get('ano')

        filme.ano = int(ano_str) if ano_str else None

        db.session.commit()

        return redirect(url_for('listar_filmes'))

    return render_template('editar.html', filme=filme)