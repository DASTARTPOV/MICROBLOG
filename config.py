import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "rs.ty4.165y.fk45.y||651fy"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False