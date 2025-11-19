from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.produto import Produto 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    todos_produtos = Produto.query.all()
    return render_template('produtos.html', produtos=todos_produtos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    preco_str = request.form.get('preco')
    qtd_str = request.form.get('quantidade')
    
    preco = float(preco_str) if preco_str else None
    quantidade = int(qtd_str) if qtd_str else None

    if nome:
        novo_produto = Produto(nome=nome, preco=preco, quantidade=quantidade)
        db.session.add(novo_produto)
        db.session.commit()

    return redirect(url_for('produtos'))

@app.route('/excluir/<int:id>')
def excluir(id):
    produto = Produto.query.get(id)

    db.session.delete(produto)
    db.session.commit()

    return redirect(url_for('produtos'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    produto = Produto.query.get(id)

    if request.method == 'POST':
        produto.nome = request.form.get('nome')
        preco_str = request.form.get('preco')
        qtd_str = request.form.get('quantidade')

        produto.preco = float(preco_str) if preco_str else None
        produto.quantidade = int(qtd_str) if qtd_str else None

        db.session.commit()

        return redirect(url_for('produtos'))

    return render_template('editar.html', produto=produto)