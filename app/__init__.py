from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sslify import SSLify

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
sslify = SSLify(app)

from api import views