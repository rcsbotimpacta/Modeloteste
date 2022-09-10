from flask import Flask,render_template,request,redirect
from models import db,Chamado



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chamado.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def Lista():
    chamado = Chamado.query.all()
    return render_template('datalist.html', chamado=chamado)

@app.route('/criarchamado', methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('criarchamado.html')

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        prioridade = request.form['prioridade']
        chamado = Chamado(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
        )
        db.session.add(chamado)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('datalist.html')

# @app.route('/')
# def RetrieveList():
#     chamado = Chamado.query.all()
#     return render_template('datalist.html', chamado=chamado)

# @app.route('/<int:id>')
# def RetrieveDespesas(id):
#     despesas = Despesas.query.filter_by(id=id).first()
#     if despesas:
#         return render_template('data.html', despesas=despesas)
#     return f"Despesas with id ={id} nao existe"


@app.route('/<int:id>/editchamado', methods=['GET','POST'])
def update(id):
    chamado = Chamado.query.filter_by(id=id).first()
    if request.method == 'POST':
        if chamado:
            db.session.delete(chamado)
            db.session.commit()

            titulo = request.form['titulo']
            descricao = request.form['descricao']
            prioridade = request.form['prioridade']
            chamado = Chamado(
                titulo=titulo,
                descricao=descricao,
                prioridade=prioridade
             )
            db.session.add(chamado)
            db.session.commit()
            return redirect('/')
            return f"Chamado com id = {id} nao existe"

    return render_template('update.html', chamado=chamado)


@app.route('/<int:id>/deletechamado', methods=['GET','POST'])
def delete(id):
    chamado = Chamado.query.filter_by(id=id).first()
    if request.method == 'POST':
        if chamado:
            db.session.delete(chamado)
            db.session.commit()
            return redirect('/')
        return abort(404)
     #return redirect('/')
    return render_template('delete.html')


@app.route('/teste')
def teste():
    return render_template('index.html')


@app.route('/teste2')
def teste2():
    return render_template('index2.html')


app.run(host='localhost', port=5000, debug=True)