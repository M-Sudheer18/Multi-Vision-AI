import os
from flask import Flask, jsonify
from flask_cors import CORS
from src.config.settings import settings
from src.utils.logger import get_logger
from flask_api.routes import (
    web_bp,
    health_bp,
    prediction_bp
)
logger = get_logger(__name__)

# Creates and configures the Flask application
def create_app() -> Flask:
    app = Flask(
        settings.APP_NAME,
        template_folder="templates",
        static_folder="static"
    )
    # Enable CORS so external apps 
    # Like Streamlit later can securely communicate with this API
    CORS(app)

    # Register the Blueprints
    app.register_blueprint(web_bp) # Web serves "/" route for your HTML page
    app.register_blueprint(health_bp, url_prefix="/api/v1") # /api/v1/health
    app.register_blueprint(prediction_bp, url_prefix="/api/v1") # /api/v1/predict

    # Global Error Handlers
    # (Keeps the API from returning ugly HTML on a crash)
    @app.errorhandler(404)
    def not_found(e):
        return jsonify(
            {
                "success": False,
                "error": "Endpoint not Found.."
            }
        )
    logger.info(f"{settings.APP_NAME} v{settings.APP_VERSION} Initialized Successfully..")
    return app

# Run Locally / Production
if __name__ == "__main__":
    app = create_app()
    logger.info("Starting Flask Server..")
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=settings.DEBUG
    )