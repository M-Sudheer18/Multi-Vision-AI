from flask import Blueprint, jsonify
from src.config.settings import settings

health_bp = Blueprint("health", __name__)
@health_bp.route('/health', methods=['GET'])
# Endpoint to verify the API is running.
def health_check():
    return jsonify(
        {
            "status": "healthy",
            "app_version": settings.APP_VERSION,
            "message": f"{settings.APP_VERSION} is Helathy and Running!.."
        }
    ), 200