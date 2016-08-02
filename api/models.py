from app import db
from geoalchemy2 import Geometry


class Hechos(db.Model):
    __tablename__ = 'hechos'
    id = db.Column(db.Integer, primary_key=True)
    mes = db.Column(db.String(20))
    lugar = db.Column(db.String(150))
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326))
    x = db.Column(db.Float)
    y = db.Column(db.Float)
