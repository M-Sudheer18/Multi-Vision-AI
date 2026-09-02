import logging
# from pathlib import Path
from typing import Dict
from tensorflow.keras.models import load_model, Model
from src.config.settings import settings
from huggingface_hub import hf_hub_download

logger = logging.getLogger(__name__)

# Hugging Face model fails to load.
class ModelLoadError(Exception):
    pass    

# class to manage the downloading, loading, and in-memory caching of Keras models directly from the Hugging Face Hub.
class HFModelLoader:
    _instance = None
    _model_cache: Dict[str, Model] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Load Model
    def load(
        self,
        repo_id: str = "Sudheer17/Image_Classifier",
        filename: str = "tuned/best_tuned_model.keras"
    ) -> Model:
        cache_key = f"{repo_id}/{filename}"

        # Memory Cache Check
        if cache_key in self._model_cache:
            if settings.DEBUG:
                logger.debug(
                    "FAST RETRIEVAL: "
                    f"Pulling model from memory cache: {cache_key}"
                )
            return self._model_cache[cache_key]

        # Download and Load from the HuggingFace
        try:
            if settings.DEBUG:
                logger.info(
                    "Loading model from Hugging Face: "
                    f"{cache_key}"
                )
            cached_model_path = hf_hub_download(
                repo_id=repo_id,
                filename=filename
            )
            logger.info(
                f"Model downloaded/cached at: "
                f"{cached_model_path}"
            )

            # Load into Keras without Optimizer for faster inference
            model = load_model(cached_model_path, compile=False)

            # Store in Ram Cache
            self._model_cache[cache_key] = model
            logger.info(f"Model successfully loaded from HF and cached: {filename}")
            return model
        except Exception as e:
            logger.exception(
                "Unable to load model from Hugging Face"
            )
            raise ModelLoadError(
                f"Failed to load model "
                f"'{filename}' from Hugging Face: {e}"
            ) from e

model_loader = HFModelLoader()