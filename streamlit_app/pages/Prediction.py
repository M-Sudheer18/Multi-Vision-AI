import requests
import streamlit as st
from components.style import load_css
from components.metrics import render_metrics
from components.sidebar import render_sidebar
from components.prediction_card import render_prediction_card
from components.probability_chart import render_probability_chart

# Without Docker
API_URL = "http://localhost:5000/api/v1/predict"

# With Docker
# API_URL = "http://flask_api:5000/api/v1/predict"
def render_prediction_page():
    """Render the Image Prediction Page.."""
    st.markdown(
        """<div class="hero-section">
            <div class="hero-badge">
                🔍 Image Prediction
            </div>
            <h1>
                Classify Your<br>
                <span>Image with AI</span>
            </h1>
            <p class="hero-description">
                Upload an image and let the trained TensorFlow CNN
                analyze it through the Flask prediction API.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        "<br>", unsafe_allow_html=True
    )

    # Upload Section
    st.markdown(
        """<div class="content-card">
            <div class="section-label">
                IMAGE INPUT
            </div>
            <h2>
                Upload an image
            </h2>
            <p>
                Select an image to send to the VisionClassify
                prediction pipeline.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    uploaded_file = st.file_uploader(
        "Choose an image..",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )
    if uploaded_file is None:
        st.info("Please upload a Image for Predition..")
        return

    # Display the Uploaded Image..
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown(
            """<div class="section-label">
                SELECTED IMAGE
            </div>
            """,
            unsafe_allow_html=True
        )
        st.image(
            uploaded_file,
            use_container_width=True
        )

    with col2:
        st.markdown(
            """
            <div class="section-label">
                READY FOR INFERENCE
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <p>
                Your image has been loaded successfully.
                Click the button below to send it to the
                Flask prediction API.
            </p>
            """,
            unsafe_allow_html=True
        )
        predict_button = st.button(
            "🚀 Predict Image",
            use_container_width=True
        )
    if not predict_button:
        return

    # Send Image to Flask API
    with st.spinner("Analyzing the Image..."):
        try:
            uploaded_file.seek(0)
            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }
            response = requests.post(
                API_URL,
                files=files,
                timeout=30
            )
            result = response.json()
        except requests.exceptions.ConnectionError:
            st.error(
                "Unable to connect to the Flask prediction API. "
                "Make sure the Flask server is running on port 5000."
            )
            return
        except requests.exceptions.Timeout:
            st.error(
                "The prediction API took too long to respond."
            )
            return

        except requests.exceptions.RequestException as e:
            st.error(
                f"API request failed: {str(e)}"
            )
            return

        except ValueError:
            st.error(
                "The prediction API returned an invalid response."
            )
            return

    # Handle API Failure Error..
    if not result.get("success", False):
        error_message = result.get(
            "error",
            "Prediction failed."
        )
        error_type = result.get(
            "error_type",
            "Unknown Error"
        )
        st.error(
            f"{error_type}: {error_message}"
        )
        return

    # Extraxct the Successful Predicion
    predicted_class = result.get(
        "predicted_class"
    )
    confidence = result.get(
        "confidence"
    )
    probabilities = result.get(
        "probabilities"
    )
    if predicted_class is None or confidence is None:
        st.error(
            "Predicted Response is missing Required Data"
        )
        return
    st.markdown("<br>", unsafe_allow_html=True)

    # Predicted Result
    st.markdown(
        """
        <div class="section-label">
            PREDICTION RESULT
        </div>
        """,
        unsafe_allow_html=True
    )
    render_prediction_card(
        predicted_class,
        confidence
    )
    st.markdown("<br>", unsafe_allow_html=True)
    render_metrics(
        predicted_class,
        f"{confidence * 100:.2f}%"
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Probability Distribution..
    render_probability_chart(
        probabilities
    )

def main():
    load_css()
    render_sidebar()
    render_prediction_page()

if __name__ == "__main__":
    main()