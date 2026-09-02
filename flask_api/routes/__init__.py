from flask_api.routes.health import health_bp
from flask_api.routes.prediction import prediction_bp
from flask_api.routes.web import web_bp

__all__ = [
    "health_bp",
    "prediction_bp",
    "web_bp"
]