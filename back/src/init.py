from flask import Flask, render_template, request
from flask_cors import CORS
from flasgger import Swagger
from src.config import Config
from src.extensions import db
from src.routes import api

def register_extensions(app):
    db.init_app(app)
    CORS(app)
    Swagger(app) 

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SWAGGER'] = {
        'title': 'MoodBoard API',
        'uiversion': 3,
        'version': '1.0',
        'description': 'API for MoodBoard',
        'termsOfService': 'Use with caution!'
    }
    register_extensions(app)
    
    app.register_blueprint(api, url_prefix='/api')

    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app