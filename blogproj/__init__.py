from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blogproj.core.views import core

app=Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db = SQLAlchemy(app)
# #Migrate(app,db)
app.register_blueprint(core)
