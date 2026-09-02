import logging
import numpy as np
from typing import Dict, List, Any
from src.config.settings import settings
from src.core.model_loader import model_loader
from src.core.preprocessing import preprocessor, ImageProcessingError

logger = logging.getLogger(__name__)

# Custom exception raised when inference fails.
class PredictionError(Exception):
    pass

# Prediction Pipeline
# Raw Bytes -> Preprocessing -> HF Model Inference -> JSON-ready Output
class ImagePredictor:
    # Executes the prediction pipeline on an uploaded image
    def predict(self, image_bytes: bytes) -> Dict[str, Any]:
        try:
            # Transform the raw bytes into a normalized (1, 32, 32, 3) numpy array
            logger.info("Starting Image Preprocessing..")
            img_array = preprocessor.process_image(image_bytes)

            # Retrieve the model
            model = model_loader.load()

            # Execute the forward pass (Inference)
            logger.info("Executing Model Prediction..")
            raw_preditions = model.predict(img_array, verbose=0)
            return self._format_results(raw_preditions[0])
        except Exception as e:
            logger.exception(f"Failed during Model Inference: {str(e)}")
            raise PredictionError(f"Failed to Predict the Image: {str(e)}")

    # Converts the raw numpy float32 output into a JSON-serializable Python dictionary.
    def _format_results(self, probabilities: np.ndarray) -> Dict[str, Any]:
        # Find the Index of the Highest Probability
        top_class_index = int(np.argmax(probabilities))
        top_class_name = settings.CLASS_NAMES[top_class_index]
        top_confidence = float(probabilities[top_class_index])

        # Creating Dictionary of all classes and their respective probabilities
        full_distributions = {
            settings.CLASS_NAMES[i]: float(prob)
            for i, prob in enumerate(probabilities)
        }
        # Sort from High to Low
        sorted_distributions = dict(
            sorted(
                full_distributions.items(),
                key = lambda item: item[1], 
                reverse=True,
            )
        )

        return {
            "success": True,
            "predicted_class": top_class_name,
            "confidence": top_confidence,
            "probabilities": sorted_distributions
        }

predictor = ImagePredictor()