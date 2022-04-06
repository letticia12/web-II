from flask import Flask
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)

host = app.config["FLASK_HOST"]
port = app.config["FLASK_PORT"]

server = Server(host=host, port=port)
manager.add_command("runserver", server)
manager.add_command("db", MigrateCommand)

from app.models.pessoa import Pessoa
from app.models.cidade import Cidade
from app.models.uf import Uf
from app.models.curso import Curso
from app.models.disciplina import Disciplina