from flask import Blueprint, jsonify, request
from src.services.prediction_service import prediction_service

prediction_bp = Blueprint('prediction', __name__)
@prediction_bp.route("/predict", methods=['POST'])
def predict():
    # Accepts the image and Get Clasiified...
    # Check whether the file is there or not...
    if 'file' not in request.files:
        return jsonify({
            "success": False,
            "error": "No file included in the Request",
            "error_type": "BadRequest"
        }), 400
    file = request.files['file']

    # Check Form is Empty or Cantains any Data
    if file.filename == "":
        return jsonify({
            "success": False,
            "error": "No File Selected for Uploading..",
            "error_type": "BadRequest"
        }), 400
    # Read the Data
    file_bytes = file.read()
    result = prediction_service.process_and_predict(
        file.filename, 
        file_bytes
    )
    # Success = 200 or Bad Request = 400
    status_code = 200 if result.get("success") else 400
    return jsonify(result), status_code