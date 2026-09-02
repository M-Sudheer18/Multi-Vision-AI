from pathlib import Path
from typing import Tuple
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Application configuration managed by Pydantic.
# Values can be overridden by environment variables in a .env file.
class Settings(BaseSettings):
    # App Config
    APP_NAME: str = "Image Classifier"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = Field(default=False, description="Enable debug mode for verbose logging") 
    # Model Config
    # MODEL_PATH: Path = BASE_DIR / "models" / "tuned" / "best_tuned_model.keras"
    MODEL_DIR: Path = (
        BASE_DIR / "models"
    )
    # Default Model
    MODEL_PATH: Path = (
        MODEL_DIR
        / "tuned"
        / "best_tuned_model.keras"
    )
    # Available Models
    BASELINE_MODEL_PATH: Path = (
        MODEL_DIR
        / "baseline"
        / "model.keras"
    )
    TUNED_MODEL_PATH: Path = (
        MODEL_DIR
        / "tuned"
        / "best_tuned_model.keras"
    )
    HYPERPARAMETER_MODEL_PATH: Path = (
        MODEL_DIR
        / "model_hp.keras"
    )
    HF_REPO_ID: str = (
        "Sudheer17/Image_Classifier"
    )
    HF_MODEL_FILES: dict = {
        "baseline": "baseline/model.keras",
        "tuned": "tuned/best_tuned_model.keras",
        "hyperparameter": "model_hp.keras"
    }
    # Image Processing Config
    IMAGE_SIZE: Tuple[int, int] = (32, 32)
    CHANNELS: int = 3

    # Using a Tuple instead of a List makes this immutable
    CLASS_NAMES: Tuple[str, ...] = (
        "airplane",
        "automobile",
        "bird",
        "cat",
        "deer",
        "dog",
        "frog",
        "horse",
        "ship",
        "truck"
    )
    # File Upload Configuration
    MAX_FILE_SIZE_MB: int = 5
    ALLOWED_EXTENSIONS: Tuple[str, ...] = (
        ".jpg",
        ".jpeg",
        ".png",
        ".webp"
    )
    # Pydantic Settings Configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )
settings = Settings()