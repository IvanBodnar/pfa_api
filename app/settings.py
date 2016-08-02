DEBUG = True
DB_USER = 'ivan'
DB_PASSWORD = 'ivan'
DB_NAME = 'pfa_api'
DB_HOST = 'localhost'
DB_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = DB_URI