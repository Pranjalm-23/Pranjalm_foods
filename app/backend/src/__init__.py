# src/__init__.py

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a secure random key

    # Setting up logging
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)
    file_handler = RotatingFileHandler(r'../../logs/backend_application.log', maxBytes=100000, backupCount=1)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Register blueprints for different components here
    from src.routes.auth import auth_bp
    from src.routes.vendor import vendor_bp
    from src.routes.menu import menu_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(vendor_bp)
    app.register_blueprint(menu_bp)

    return app
