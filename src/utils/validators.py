import os
from src.config.settings import settings

# Getting More Detailed Error Exception during Code Runnig...
class ValidationError(Exception):
    pass

# Validate the File On the Basis of Setting.py
def validate_uploaded_file(filename: str, file_data: bytes) -> bool:
    # Check the Extention and also Extract it and Lower Case it
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    if extension not in settings.ALLOWED_EXTENSIONS:
        raise ValidationError(
            f"Invalid File Type: {extension}. "
            f"Allowed Types: {', '.join(settings.ALLOWED_EXTENSIONS)}"
        )

    # Check the File Size and Convert Bytes to MB
    file_size_mb = len(file_data) / (1024 * 1024)
    if file_size_mb > settings.MAX_FILE_SIZE_MB:
        raise ValidationError(
            f"File size ({file_size_mb:.2f} MB) exceeds the "
            f"maximum allowed size of {settings.MAX_FILE_SIZE_MB} MB."
        )
    return True