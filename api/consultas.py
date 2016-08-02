from geojson import Feature, Point, FeatureCollection
from app import db


class Consultas:

    def __init__(self, tabla):
        self.pfa = tabla

    @staticmethod
    def make_geojson(query):
        features = []

        for item in query:
            try:
                point = Point((item.x, item.y))
                feature = Feature(geometry=point,
                                  properties={'id': item.id, 'mes': item.mes, 'lugar': item.lugar})
                features.append(feature)
            except ValueError:
                pass

        return FeatureCollection(features)

    def consulta_prueba(self):
        consulta = self.make_geojson(self.pfa.query.limit(20))
        return consulta

    def consulta_mes(self, mes):
        consulta = self.make_geojson(self.pfa.query.filter_by(mes=mes))
        return consulta

    def consulta_espacial(self):
        sql = 'select * from hechos' \
              ' where ST_DWithin(ST_Transform(geom, 97124),' \
              ' ST_Transform(ST_SetSRID(ST_MakePoint(-58.4688709698659, -34.629732201265)' \
              ', 4326), 97124), 150);'
        result = db.engine.execute(sql)
        return self.make_geojson(result)