from typing import Dict, Any
from src.utils.logger import get_logger
from src.utils.validators import validate_uploaded_file, ValidationError
from src.core.predictor import predictor, PredictionError
from src.core.preprocessing import ImageProcessingError

logger = get_logger(__name__)

class PredictionService:
    @staticmethod
    def process_and_predict(filename: str, file_data: bytes) -> Dict[str, Any]:
        # Runs the full pipeline for an incoming image request
        logger.info(f"Incoming Prediction Request for file: {filename}")
        try:
            # Security is File Really Safe
            validate_uploaded_file(filename, file_data)
            logger.info("File Validation Success.. Routing to Process and Predict..")
            # Process and Predict
            result = predictor.predict(file_data)
            logger.info("Prediction Completed. Returning Results")
            return result
        except ValidationError as ve:
            logger.warning(f"Validation Error Occurs for: {filename}: {str(ve)}")
            return {
                "success": False,
                "error": str(ve),
                "error_type": "ValidationError"
            }
        except ImageProcessingError as ie:
            logger.warning(f"Processing Error: {filename}: {str(ie)}")
            return {
                "success": False,
                "error": str(ie),
                "error_type": "ImageProcessingError"
            }
        except PredictionError as pe:
            logger.error(f"Prediction Error: {filename}: {str(pe)}")
            return {
                "success": False,
                "error": str(pe),
                "error_type": "PredictionError"
            }
        except Exception as e:
            logger.critical(f"Unexpected Critical Error: {filename}: {str(e)}")
            return {
                "success": False,
                "error": "An unexpected internal server error occurred.",
                "error_type": "Internal Error"
            }
prediction_service = PredictionService()