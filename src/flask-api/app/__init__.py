import logging
import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Define log directory and file
    log_dir = r"E:\NIDS-model\src\flask-api\data\logs"
    os.makedirs(log_dir, exist_ok=True)  # Create directory if it doesn't exist
    log_file = os.path.join(log_dir, "app.log")
    
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),      # Log to console
            logging.FileHandler(log_file)   # Log to file in mounted volume
        ]
    )
    
    from app.routes import api
    app.register_blueprint(api, url_prefix="/api")
    return app
