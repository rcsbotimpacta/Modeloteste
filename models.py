from flask_sqlalchemy import SQLAlchemy


db =SQLAlchemy()


class Chamado(db.Model):
    __tablename__ = "chamado"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.String(1000))
    prioridade = db.Column(db.String(100))

    def __init__(self, titulo, descricao, prioridade):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade


    def __repr__(self):
        return f"{self.titulo}:{self.prioridade}"

