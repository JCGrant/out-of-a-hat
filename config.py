import os

base_dir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = 'True'
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')
    SERVER_NAME = '127.0.0.1:5000'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SERVER_NAME = 'http://out-of-a-hat.herokuapp.com:80'
