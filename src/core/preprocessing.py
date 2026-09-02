import io
import logging
import numpy as np
from PIL import Image, UnidentifiedImageError
from src.config.settings import settings

logger = logging.getLogger(__name__)

# Custom exception raised when an image fails to process.
class ImageProcessingError(Exception):
    pass

# Handles the transformation of raw uploaded images into the exact
# mathematical format expected by the CIFAR-10 Keras model
class ImagePreprocessor:
    @staticmethod
    def process_image(image_bytes: bytes) -> np.ndarray:
        # Reads raw bytes, resizes, and normalizes the image.
        try:
            # Open the image from Ram(No Saving Req)
            image = Image.open(
                io.BytesIO(image_bytes)
            )
            # Ensure the Image is RGB
            if image.mode != "RGB":
                image = image.convert("RGB")

            # Resizing the Image 
            image = image.resize(
                settings.IMAGE_SIZE
            )

            # Convert to a Array
            img_array = np.asarray(
                image,
                dtype=np.float32
            )
            # Normalizing Array
            img_array /= 255.0
            # Expanding Dimentions to create a Batch of `1`
            img_array = np.expand_dims(img_array, axis = 0)
            logger.debug(
                "Image processed successfully. "
                f"Shape: {img_array.shape}"
            )
            return img_array
        except UnidentifiedImageError as e:
            logger.error("Uploaded file is not a valid image format.")
            raise ImageProcessingError("The uploaded file is not a valid image.") from e
        except Exception as e:
            logger.exception(f"Unexpected error during image processing: {str(e)}")
            raise ImageProcessingError(f"Failed to process image: {str(e)}") from e

preprocessor = ImagePreprocessor()