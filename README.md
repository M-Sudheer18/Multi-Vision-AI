<div align="center">

# 🚀 MultiVision AI

### Multi-Class Image Classification — TensorFlow CNN · Flask API · Streamlit UI · Docker

An AI-powered image classification application. Upload an image and instantly get a **CNN-based prediction** with a **confidence score** and a **full probability distribution** across all 10 CIFAR-10 classes — served through a Flask REST API and an interactive Streamlit frontend, fully containerized with Docker.

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-CNN-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

[Live App](https://multi-vision-ai.streamlit.app/) · [API](https://multivision-ai-api.onrender.com/) · [Report](./REPORT.md) · [Issues](https://github.com/sudheermuthyala/multivision-ai/issues)

</div>

---

## 📖 Overview

**MultiVision AI** takes a trained TensorFlow CNN model and wraps it in a complete, production-style application. Upload an image, and the app validates it, preprocesses it, runs inference, and returns the predicted class with a confidence score and full probability distribution — all in real time.

> Live App and API links above are the actual deployed endpoints. The GitHub repo link is a placeholder — update it once your repository is public.

---

## ✨ Features

- 📤 Upload **JPG / JPEG / PNG** images for instant classification
- 🧠 CNN-based prediction across 10 CIFAR-10 classes
- 🎯 Predicted class label + 📊 confidence score
- 📈 Full probability distribution across all classes
- 🔌 Lightweight Flask REST API (health check + prediction endpoint)
- 🖥️ Clean, interactive Streamlit interface
- 🐳 One-command Docker + Docker Compose setup
- ❤️ API health-check endpoint
- ☁️ Cloud-deployed frontend and backend

---

## 🗂️ Supported Categories (CIFAR-10)

| ✈️ Airplane | 🚗 Automobile | 🐦 Bird | 🐱 Cat | 🦌 Deer |
|:---:|:---:|:---:|:---:|:---:|
| 🐶 **Dog** | 🐸 **Frog** | 🐴 **Horse** | 🚢 **Ship** | 🚚 **Truck** |

---

## 🏗️ Architecture

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

| Layer | Responsibility |
|---|---|
| **Frontend** (Streamlit) | UI, image upload, calling the API, displaying results |
| **Backend** (Flask) | Routing, validation, preprocessing, running inference, JSON responses |
| **Model** (TensorFlow CNN) | Classifying images and computing class probabilities |

### 🔄 Prediction Pipeline

```text
Upload Image → Image Validation → Image Preprocessing (RGB → 32×32 → Normalize)
   → TensorFlow CNN Model → Prediction Probabilities → Predicted Class + Confidence
```

---

## 🧰 Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Deep Learning | TensorFlow, Keras |
| Data / Imaging | NumPy, Pillow |
| Backend | Flask, Flask-CORS |
| Frontend | Streamlit |
| Networking | Requests |
| DevOps | Docker, Docker Compose |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```text
MultiVision-AI/
│
├── flask_api/
│   ├── routes/            # health.py, prediction.py, web.py
│   ├── src/                # config, core, services, utils, validators
│   ├── templates/
│   ├── static/
│   └── app.py
│
├── streamlit_app/
│   ├── components/
│   ├── pages/              # Prediction.py, Performance.py, ...
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

## ⚙️ Prerequisites

**Local Execution (No Docker)**
- ✅ Python **3.13** (or compatible version)
- ✅ Git
- ✅ pip

**Docker Execution**
- ✅ Docker Desktop
- ✅ Docker Compose

---

## 💻 Run Locally (Recommended for Development)

**1) Clone the repository**
```bash
git clone https://github.com/sudheermuthyala/multivision-ai.git
cd multivision-ai
```

**2) Create & activate a virtual environment**

Windows (Command Prompt):
```bash
python -m venv image_venv
image_venv\Scripts\activate
```

Windows (PowerShell):
```bash
python -m venv image_venv
.\image_venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv image_venv
source image_venv/bin/activate
```

You should see `(image_venv)` at the start of your terminal prompt.

**3) Install dependencies**
```bash
pip install -r requirements.txt
```

**4) Start the Flask API** (Terminal 1)
```bash
cd flask_api
flask run
```
API runs on `http://127.0.0.1:5000`

**5) Start the Streamlit UI** (Terminal 2)
```bash
cd streamlit_app
streamlit run app.py
```
UI runs on `http://localhost:8501`

### 🔗 Local URLs Summary

| Service | URL |
|---|---|
| Streamlit Application | `http://localhost:8501` |
| Flask API | `http://127.0.0.1:5000` |
| API Health Check | `http://127.0.0.1:5000/api/v1/health` |

---

## 🔌 API Reference

### ❤️ Health Check
```http
GET /api/v1/health
```
```json
{
  "status": "healthy",
  "app_version": "application_version",
  "message": "Application is Healthy and Running"
}
```

### 🖼️ Predict
```http
POST /api/v1/predict
```
Accepts an uploaded file in form-data field: `file` (JPG / JPEG / PNG)

**Response**
```json
{
  "success": true,
  "predicted_class": "Ship",
  "confidence": 0.80,
  "probabilities": {
    "Airplane": 0.02,
    "Automobile": 0.01,
    "Bird": 0.05,
    "Cat": 0.03,
    "Deer": 0.01,
    "Dog": 0.02,
    "Frog": 0.01,
    "Horse": 0.03,
    "Ship": 0.80,
    "Truck": 0.02
  }
}
```

---

## 🐳 Run Using Docker (Full Container Setup)

**1) Verify Docker**
```bash
docker --version
docker compose version
```

**2) Update the Streamlit API URL for Docker networking**

In `streamlit_app/pages/Prediction.py`, set:
```python
API_URL = "http://flask_api:5000/api/v1/predict"
```
and comment out the localhost version:
```python
# API_URL = "http://localhost:5000/api/v1/predict"
```

**3) Build & start** (from project root)
```bash
docker compose up --build
```

| Service | URL |
|---|---|
| Streamlit | `http://localhost:8501` |
| Flask API | `http://localhost:5000` |

**4) Stop containers**
```bash
docker compose down
```
(or press `CTRL + C`)

**5) Remove containers & images / clean build cache**
```bash
docker compose down --rmi all
docker builder prune -a
```

### 🔄 Switching Between Local and Docker

| Mode | `API_URL` |
|---|---|
| Local | `http://localhost:5000/api/v1/predict` |
| Docker | `http://flask_api:5000/api/v1/predict` |

---

## ☁️ Deployment

| Component | Platform | Status | URL |
|---|---|---|---|
| Frontend | Streamlit Community Cloud | ✅ Deployed | `https://multi-vision-ai.streamlit.app/` |
| Backend | Render | ✅ Deployed | `https://multivision-ai-api.onrender.com/` |
| Infrastructure | AWS (EC2 / ECS / App Runner) | 🔮 Optional / Future | — |

**Environment-based configuration:**
```text
# Local
API_URL=http://localhost:5000/api/v1/predict

# Docker
API_URL=http://flask_api:5000/api/v1/predict

# Production
API_URL=https://multivision-ai-api.onrender.com/api/v1/predict
```

---

## 💡 Use Cases

- 🧠 Deep learning image classification demos
- 🎓 Machine learning / AI coursework
- 📚 Learning the CNN + TensorFlow workflow
- 🔌 REST API-based ML applications
- 🖥️ Interactive AI web apps
- 🐳 Dockerized ML deployments
- 💼 Portfolio and resume projects

---

## 📌 Notes / Important

- ✅ During local execution, the Flask API must be running before predicting.
- ✅ Streamlit communicates with the Flask API for inference.
- ⚙️ TensorFlow may fall back to **CPU** if GPU/CUDA is unavailable.
- ✅ Docker requires Docker Desktop to be running.

---

## 🗺️ Roadmap

- [ ] Improve CNN architecture and model accuracy (transfer learning, augmentation)
- [ ] Add authentication for secure access
- [ ] Persist prediction history in a database
- [ ] Add cloud storage for uploads (S3 / Cloudinary)
- [ ] CI/CD pipeline with GitHub Actions
- [ ] Optional AWS migration

---

## 📚 Documentation

For full details including dataset preparation, model training, CNN architecture, image preprocessing, backend/frontend architecture, API integration, Docker implementation, and challenges & solutions, see **[REPORT.md](./REPORT.md)**.

---

## 🤝 Contributing

Contributions are welcome. Fork the repo, create a feature branch, and open a pull request describing your changes.

## 📄 License

Released under the [MIT License](./LICENSE).

## 👨‍💻 Author

**Sudheer Muthyala**

---

<div align="center">

⭐ If you found this project helpful, consider giving it a star on GitHub.

Made with TensorFlow · Flask · Streamlit · Docker

</div>
