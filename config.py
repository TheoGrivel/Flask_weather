import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SERET_KEY') or 'Joost8gr'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'theo_weer.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # elke wijziging in de gaten houden... hoeft niet