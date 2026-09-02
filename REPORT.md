# 📘 REPORT — MultiVision AI
### Multi Image Classification System — End-to-End Deep Learning Application

---

## 📋 Table of Contents

1. [Project Overview](#1-project-overview)
2. [Problem Statement](#2-problem-statement)
3. [Project Objective](#3-project-objective)
4. [Project Scope](#4-project-scope)
5. [Technology Stack](#5-technology-stack)
6. [System Architecture](#6-system-architecture)
7. [Dataset](#7-dataset)
8. [Image Categories](#8-image-categories)
9. [Project Development Workflow](#9-project-development-workflow)
10. [Project Structure](#10-project-structure)
11. [Deep Learning Model](#11-deep-learning-model)
12. [Image Preprocessing](#12-image-preprocessing)
13. [Flask Backend Development](#13-flask-backend-development)
14. [REST API Implementation](#14-rest-api-implementation)
15. [Prediction Pipeline](#15-prediction-pipeline)
16. [Streamlit Frontend Development](#16-streamlit-frontend-development)
17. [Frontend and Backend Integration](#17-frontend-and-backend-integration)
18. [Application Workflow](#18-application-workflow)
19. [Error Handling](#19-error-handling)
20. [Docker Integration](#20-docker-integration)
21. [Running the Application Locally](#21-running-the-application-locally)
22. [Running the Application with Docker](#22-running-the-application-with-docker)
23. [Deployment Architecture](#23-deployment-architecture)
24. [Streamlit Deployment](#24-streamlit-deployment)
25. [Flask API Deployment](#25-flask-api-deployment)
26. [AWS Deployment](#26-aws-deployment)
27. [Deployment Roadmap](#27-deployment-roadmap)
28. [Deployment Configuration](#28-deployment-configuration)
29. [Production Considerations](#29-production-considerations)
30. [Challenges and Solutions](#30-challenges-and-solutions)
31. [Project Results](#31-project-results)
32. [Project Achievements](#32-project-achievements)
33. [Key Learning Outcomes](#33-key-learning-outcomes)
34. [Future Improvements](#34-future-improvements)
35. [Conclusion](#35-conclusion)
36. [Project Links](#36-project-links)
37. [Author & Project Status](#37-author--project-status)

---

# 1. Project Overview

**MultiVision AI** is an end-to-end deep learning image classification application designed to classify uploaded images into predefined categories.

The system integrates multiple technologies to build a complete machine learning application:

- A trained **TensorFlow CNN** model
- Image preprocessing & validation
- **Flask REST API** for prediction services
- **Streamlit** interactive frontend
- **Docker** containerization for consistent execution

**How it works:** The user uploads an image in the Streamlit UI. The image is sent to the Flask prediction API, where it is validated and processed before running inference on the CNN model. The model generates probabilities for all classes and returns the most likely predicted category along with a confidence score.

---

# 2. Problem Statement

Image classification is a core computer vision task. While deep learning models can achieve strong accuracy, building a usable application requires more than a trained model. A complete machine learning system must support:

- Image upload
- File validation
- Image preprocessing
- Model loading & inference
- Probability computation
- API communication
- UI design
- Deployment readiness

This project focuses on creating the full pipeline — from model inference to a working, deployable application.

---

# 3. Project Objective

The main objective is to develop an end-to-end image classification application using deep learning. The system allows users to:

1. Upload an image
2. Validate the uploaded file
3. Preprocess the image for model input
4. Send it to the CNN model for inference
5. Generate prediction probabilities for supported classes
6. Select the highest probability class
7. Display predicted class and confidence score
8. Show probability distribution
9. Use a user-friendly web interface

Additional objectives include building a REST API, separating frontend/backend responsibilities, and enabling containerized execution.

---

# 4. Project Scope

The project supports image classification using a trained Convolutional Neural Network.

- Dataset: **CIFAR-10**
- Output: classification among **10 categories**
- Includes:
  - Model integration
  - Preprocessing + validation
  - Flask REST API
  - Streamlit frontend
  - Docker containerization
  - Deployment preparation

This is designed as a learning and portfolio project demonstrating ML-to-production style architecture.

---

# 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| TensorFlow | Deep learning framework |
| Keras | CNN model development |
| NumPy | Numerical computations |
| Pillow | Image processing |
| Flask | REST API backend |
| Flask-CORS | Cross-origin support |
| Streamlit | Interactive frontend |
| Requests | Frontend-to-API communication |
| Docker | Containerization |
| Docker Compose | Multi-service orchestration |
| Git / GitHub | Version control & hosting |

---

# 6. System Architecture

```text
                     USER
                       │
                       ▼
              STREAMLIT FRONTEND
                       │
                Image Upload
                       ▼
               FLASK REST API
                       │
               File validation
                       ▼
             Image preprocessing
                       ▼
              TensorFlow CNN Model
                       ▼
           Prediction probabilities
                       ▼
              JSON API response
                       ▼
              Streamlit displays result
```

**Frontend (Streamlit)**
- Handles UI, uploads image, sends request to Flask API, and displays predicted class, confidence, and probabilities.

**Backend (Flask)**
- Provides API endpoints, validates request data, preprocesses image, runs CNN inference, and returns prediction JSON response.

**ML Model (TensorFlow CNN)**
- Classifies images, computes probability distribution, and selects the final prediction based on max probability.

---

# 7. Dataset

The project uses the **CIFAR-10 dataset**, which contains color images categorized into 10 classes. The CNN in this project is trained to classify images into these categories.

---

# 8. Image Categories

| Class | Category |
|---:|---|
| 1 | ✈️ Airplane |
| 2 | 🚗 Automobile |
| 3 | 🐦 Bird |
| 4 | 🐱 Cat |
| 5 | 🦌 Deer |
| 6 | 🐶 Dog |
| 7 | 🐸 Frog |
| 8 | 🐴 Horse |
| 9 | 🚢 Ship |
| 10 | 🚚 Truck |

The CNN generates a probability for each class, and the highest probability becomes the predicted label.

---

# 9. Project Development Workflow

```text
Dataset → Data Preparation → CNN Model Development → Model Training
   → Model Saving → Flask Backend Development → Prediction API Development
   → Streamlit Frontend Development → Frontend + Backend Integration
   → Docker Containerization → Deployment Preparation
```

---

# 10. Project Structure

```text
MultiVision-AI/
│
├── flask_api/
│   ├── routes/
│   │   ├── health.py
│   │   ├── prediction.py
│   │   └── web.py
│   ├── src/
│   │   ├── config/
│   │   ├── core/
│   │   ├── services/
│   │   ├── utils/
│   │   └── validators/
│   ├── templates/
│   ├── static/
│   └── app.py
│
├── streamlit_app/
│   ├── components/
│   ├── pages/
│   │   ├── Prediction.py
│   │   ├── Performance.py
│   │   └── ...
│   ├── assets/
│   └── app.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── README.md
└── REPORT.md
```

---

# 11. Deep Learning Model

The core component is a **Convolutional Neural Network (CNN)**. CNNs automatically learn visual features such as edges, shapes, textures, and object patterns.

**Example prediction (probabilities):**
```text
Airplane      → 0.02
Automobile    → 0.01
Bird          → 0.05
Cat           → 0.03
Deer          → 0.01
Dog           → 0.02
Frog          → 0.01
Horse         → 0.03
Ship          → 0.80
Truck         → 0.02
```

The class with the highest probability becomes the final output.

---

# 12. Image Preprocessing

Uploaded images cannot be directly passed to the CNN. Preprocessing ensures consistent input.

```text
Uploaded Image → Read Image Data → Convert Image to RGB → Resize to 32×32
   → Normalization → Model Input
```

Steps include:
- RGB conversion for consistent color handling
- Resize to **32 × 32**
- Normalize pixel values before inference

---

# 13. Flask Backend Development

The Flask backend provides API endpoints using a structured, Blueprint-style modular routing approach.

Key responsibilities:
- Create and configure the Flask application
- Enable CORS
- Register API routes
- Handle errors
- Configure logging

Main entry point: `flask_api/app.py`

---

# 14. REST API Implementation

The backend exposes two main endpoints.

**✅ Health Check** — `GET /api/v1/health`
```json
{
  "status": "healthy",
  "app_version": "application_version",
  "message": "Application is Healthy and Running"
}
```
Used for monitoring and deployment verification.

**🖼️ Prediction Endpoint** — `POST /api/v1/predict`

Accepts a file in the form-data field `file`.

Prediction flow: validate request payload → read image bytes → preprocess image → run CNN inference → return JSON response.

---

# 15. Prediction Pipeline

```text
User uploads image → Streamlit sends HTTP POST request → Flask prediction endpoint
   → File validation → Image preprocessing → TensorFlow CNN inference
   → Probability distribution → Highest probability class → JSON response → UI displays result
```

Returned response includes: success status, predicted class, confidence score, and probabilities for all classes.

---

# 16. Streamlit Frontend Development

The frontend is built using **Streamlit**, which provides a fast way to build ML UIs.

Streamlit components include:
- Landing page (`app.py`)
- Prediction page for uploading images
- Display of predicted class and confidence
- Probability visualization (distribution)

Main entry points:
- `streamlit_app/app.py`
- Prediction page: `streamlit_app/pages/Prediction.py`

---

# 17. Frontend and Backend Integration

Streamlit communicates with Flask using the Python **requests** library.

- **Local mode:** `http://localhost:5000/api/v1/predict`
- **Docker mode:** `http://flask_api:5000/api/v1/predict` (Compose service name)

---

# 18. Application Workflow

1. Open the Streamlit UI (`http://localhost:8501`)
2. Go to the Prediction page
3. Upload an image (JPG/JPEG/PNG)
4. Preview the image in the UI
5. Click **Predict Image**
6. Streamlit sends the file to the Flask API `/api/v1/predict`
7. Flask validates, preprocesses, and runs inference
8. Streamlit displays the predicted category, confidence score, and probability distribution

---

# 19. Error Handling

**Backend errors:** missing file field, empty file, invalid endpoints (global 404 handler).

**Frontend errors:** API connection failure (Flask not running), API timeouts, invalid API response parsing, prediction failure responses (`success=false`).

---

# 20. Docker Integration

Docker packages the environment for consistent execution.

Files: `Dockerfile`, `docker-compose.yml`, `.dockerignore`

---

# 21. Running the Application Locally

**Flask API (Terminal 1)**
```bash
cd flask_api
flask run
```
API URL: `http://127.0.0.1:5000`

**Streamlit UI (Terminal 2)**
```bash
cd streamlit_app
streamlit run app.py
```
UI URL: `http://localhost:8501`

---

# 22. Running the Application with Docker

```bash
docker compose up --build
```

- Streamlit: `http://localhost:8501`
- Flask API: `http://localhost:5000`

Stop containers:
```bash
docker compose down
```

Cleanup:
```bash
docker compose down --rmi all
docker builder prune -a
```

---

# 23. Deployment Architecture

```text
INTERNET
  ↓
STREAMLIT CLOUD
  ↓  (HTTPS request)
FLASK API (Render)
  ↓
TensorFlow CNN Model
  ↓
Prediction response
```

---

# 24. Streamlit Deployment

**Status:** ✅ Completed

Deployed via Streamlit Community Cloud, connected to the GitHub repository, with entry point `streamlit_app/app.py`.

Application URL: **https://multivision-ai.streamlit.app** *(sample link — replace with your real deployed URL)*

---

# 25. Flask API Deployment

**Status:** ✅ Completed

Deployed on **Render**.

API URL: **https://multivision-ai-api.onrender.com** *(sample link — replace with your real deployed URL)*

---

# 26. AWS Deployment

**Status:** 🔮 Optional / Future Enhancement

Possible AWS services for a future migration: EC2, Elastic Beanstalk, ECS, App Runner.

---

# 27. Deployment Roadmap

```text
Project Development → Local Testing → Docker Testing → Push Project to GitHub
   → Deploy Flask API → Get Public Backend API URL → Update Streamlit API Configuration
   → Deploy Streamlit Frontend → Test Complete Cloud Application
   → Update README.md and REPORT.md → Optional AWS Deployment
```

---

# 28. Deployment Configuration

During local development, Streamlit communicates with Flask using:
```python
API_URL = "http://localhost:5000/api/v1/predict"
```

During Docker execution, the app uses the Compose service name:
```python
API_URL = "http://flask_api:5000/api/v1/predict"
```

After deploying the Flask API to the cloud, the URL is updated to the deployed backend:
```python
API_URL = "https://multivision-ai-api.onrender.com/api/v1/predict"
```

---

# 29. Production Considerations

**Environment Variables**
The backend API URL is stored as an environment variable so the app can switch between local, Docker, and production environments without code changes:
```text
API_URL=https://your-backend-api-url
```

**Production Server** — The Flask development server is used locally only; production deployment uses the server configuration provided by the hosting platform.

**CORS Configuration** — Since the Streamlit frontend and Flask backend run on different domains after deployment, CORS is configured to allow secure cross-origin communication.

**Model Availability** — The trained TensorFlow model is bundled with the backend so the deployed service can load the model, process uploads, run inference, and return results.

---

# 30. Challenges and Solutions

| Challenge | Solution |
|---|---|
| Frontend & backend communication | Use `requests` in Streamlit to call the Flask prediction endpoint |
| Image validation | Backend checks file presence and proper form-data key |
| Image preprocessing mismatch | Convert to RGB + resize to 32×32 + normalize, matching training pipeline |
| Docker networking (localhost issue) | Use the Compose service name `flask_api` instead of `localhost` |
| Running multiple services | Use Docker Compose to run Flask + Streamlit together |
| Docker storage growth | Regular Docker cleanup and build-cache pruning |

---

# 31. Project Results

The project successfully integrates:
- Image upload + preview
- Image validation and preprocessing
- CNN-based classification with confidence score and probability distribution
- Flask REST API (health + predict)
- Streamlit UI
- Frontend-backend integration
- Docker containerization
- Local, Docker, and cloud deployment testing

---

# 32. Project Achievements

- ✅ **Deep Learning Integration** — a trained TensorFlow CNN model integrated into a real application workflow
- ✅ **Image Classification** — classifies uploaded images into CIFAR-10 categories
- ✅ **Backend API Development** — health monitoring, prediction requests, validation, error handling
- ✅ **Interactive Frontend** — upload, preview, prediction execution, results, confidence, probability visualization
- ✅ **Frontend/Backend Integration** — communication via HTTP requests
- ✅ **Docker Containerization** — multi-service orchestration with Docker Compose
- ✅ **Testing** — verified locally, in Docker, and in the cloud

---

# 33. Key Learning Outcomes

**Machine Learning:** CNNs, image classification, TensorFlow, model inference, probability prediction, CIFAR-10

**Backend Development:** Flask, REST APIs, Blueprints, routing, validation, error handling, JSON responses, CORS

**Frontend Development:** Streamlit, file uploads, UI development, API integration, prediction visualization

**Software Engineering:** modular project structure, frontend/backend separation, service-based architecture, logging, error handling

**DevOps:** Docker, Dockerfile, Docker Compose, container networking, build cache management, cleanup

**Deployment:** GitHub repository management, Streamlit Cloud deployment, backend cloud deployment (Render), AWS deployment planning

---

# 34. Future Improvements

- Improve CNN architecture / model accuracy
- Data augmentation + hyperparameter tuning / transfer learning
- Add authentication for secure access
- Store prediction history in a database
- Add cloud storage for uploaded images (S3 / Cloudinary)
- CI/CD pipeline using GitHub Actions
- Optional AWS migration (EC2 / ECS / App Runner)

---

# 35. Conclusion

**MultiVision AI** is a complete, end-to-end machine learning application that demonstrates how a trained CNN model can be turned into a production-style architecture using Deep Learning + Image Processing + Flask REST API + Streamlit UI + Docker.

```text
User Uploads Image → Streamlit Frontend → Flask Prediction API → Image Validation
   → Image Preprocessing → TensorFlow CNN Model → Prediction Probabilities
   → Highest Probability Selection → JSON API Response → Streamlit Visualization
   → Final Prediction Result
```

Users can upload an image and receive a full classification result including confidence and probabilities. The project has been developed, tested locally and with Docker, and deployed to the cloud, providing a strong base for future work such as authentication, database integration, and model upgrades.

---

# 36. Project Links

> ✅ **Deployment Status**
> The application has been successfully developed, tested locally, tested with Docker, and deployed to the cloud.

## 🔗 GitHub Repository
**Status:** ✅ Completed
Repository URL: **https://github.com/sudheermuthyala/multivision-ai** *(sample link — replace with your real repo URL)*

## 🌐 Streamlit Application
**Status:** ✅ Completed
Application URL: **https://multivision-ai.streamlit.app** *(sample link — replace with your real deployed URL)*

## ⚙️ Flask API
**Status:** ✅ Completed
API URL: **https://multivision-ai-api.onrender.com** *(sample link — replace with your real deployed URL)*

## ☁️ AWS Deployment
**Status:** 🔮 Optional / Future Enhancement
AWS URL: *Not applicable — not part of the current deployment plan*

---

# 37. Author & Project Status

**Author:** Sudheer Muthyala

| Milestone | Status |
|---|---|
| Development | ✅ Completed |
| Local Testing | ✅ Completed |
| Docker Testing | ✅ Completed |
| GitHub Repository | ✅ Completed |
| Flask Cloud Deployment | ✅ Completed |
| Streamlit Deployment | ✅ Completed |
| AWS Deployment | 🔮 Optional / Future |

---

## 🚀 MultiVision AI — From Image Upload to AI Prediction

MultiVision AI demonstrates how a deep learning model can be transformed into a complete, interactive, and deployed machine learning application.
