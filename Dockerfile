# Use Python 3.13 as the base image
# Create our container using Python 3.13.
FROM python:3.13-slim

# Set the working directory inside Docker
WORKDIR /app

# Copy requirements.txt first
COPY requirements.txt .

# Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the complete project into the container
COPY . .

# Keep Python output visible in Docker logs
ENV PYTHONUNBUFFERED=1