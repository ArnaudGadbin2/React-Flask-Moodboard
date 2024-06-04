from flask import Flask, render_template, request
from flask_cors import CORS
from config import Config
from extensions import db
from routes import api

def register_extensions(app):
    db.init_app(app) 

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)
    
    register_extensions(app)
    
    app.register_blueprint(api, url_prefix='/api')

    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app