from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Guys quit posting our key' # Our app key, DON'T POST ON GITHUB
app.config['IMAGE_UPLOADS'] = join(dirname(realpath(__file__)), 'static/imgs/')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.sqlite3'
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

#modules import
from classroom_manager.routes import *
from classroom_manager.models import User
from classroom_manager.network import *
#db.create_all()